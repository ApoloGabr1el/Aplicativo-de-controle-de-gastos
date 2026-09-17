import hashlib

from sqlalchemy.exc import IntegrityError

from Controle_gastos.banco import Session, Usuario


def senha_segura(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


def validar_login(email, senha):
    session = Session()
    try:
        usuario = session.query(Usuario).filter_by(
            email=email, senha=senha_segura(senha)
        ).first()
        if usuario is None:
            return None
        return (usuario.id, usuario.nome, usuario.email, usuario.senha)
    finally:
        session.close()


def cadastrar_usuario(nome, email, senha):
    if not nome or not email or not senha:
        return False, "Preencha todos os campos"

    session = Session()
    try:
        if session.query(Usuario.id).filter_by(email=email).first():
            return False, "Este email já está cadastrado."

        session.add(Usuario(nome=nome, email=email, senha=senha_segura(senha)))
        session.commit()
        return True, "Usuário cadastrado com sucesso!"
    except IntegrityError:
        session.rollback()
        return False, "Este email já está cadastrado."
    except Exception:
        session.rollback()
        return False, "Erro ao cadastrar usuário. Tente novamente."
    finally:
        session.close()