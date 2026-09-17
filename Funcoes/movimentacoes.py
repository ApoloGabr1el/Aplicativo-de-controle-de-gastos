from datetime import date

from sqlalchemy import func

from Controle_gastos.banco import Gasto, Session


def registrar_movimentacao(usuario_id, tipo, descricao, valor, categoria, data):
    if tipo not in ("receita", "despesa"):
        return False, "Tipo inválido. Use 'receita' ou 'despesa'."
    if not descricao or not categoria or not data:
        return False, "Preencha todos os campos."
    try:
        valor = float(valor)
    except (TypeError, ValueError):
        return False, "O valor precisa ser um número."

    if valor <= 0:
        return False, "O valor deve ser maior que zero."

    try:
        data_ok = date.fromisoformat(data) if isinstance(data, str) else data
    except ValueError:
        return False, "Data inválida. Use o formato AAAA-MM-DD."

    session = Session()
    try:
        session.add(Gasto(
            id_usuario=usuario_id,
            tipo=tipo,
            descricao=descricao,
            valor=valor,
            categoria=categoria,
            data=data_ok,
        ))
        session.commit()
        return True, f"{tipo.capitalize()} registrada com sucesso!"
    except Exception:
        session.rollback()
        return False, "Erro ao registrar a movimentação. Tente novamente."
    finally:
        session.close()


def _movimentacao_para_tupla(gasto):
    return (
        gasto.id,
        gasto.tipo,
        gasto.descricao,
        float(gasto.valor),
        gasto.categoria,
        gasto.data,
    )


def listar_movimentacoes(usuario_id, tipo=None):
    session = Session()
    try:
        query = session.query(Gasto).filter_by(id_usuario=usuario_id)
        if tipo:
            query = query.filter_by(tipo=tipo)
        gastos = query.order_by(Gasto.data.desc()).all()
        return [_movimentacao_para_tupla(g) for g in gastos]
    finally:
        session.close()


def excluir_movimentacao(id_gasto, usuario_id):
    session = Session()
    try:
        gasto = session.query(Gasto).filter_by(id=id_gasto, id_usuario=usuario_id).first()
        if gasto is None:
            return False, "Movimentação não encontrada."
        session.delete(gasto)
        session.commit()
        return True, "Movimentação excluída com sucesso!"
    except Exception:
        session.rollback()
        return False, "Erro ao excluir a movimentação. Tente novamente."
    finally:
        session.close()


def calcular_saldo(usuario_id):
    session = Session()
    try:
        total_receitas = session.query(
            func.coalesce(func.sum(Gasto.valor), 0)
        ).filter_by(id_usuario=usuario_id, tipo="receita").scalar()
        total_despesas = session.query(
            func.coalesce(func.sum(Gasto.valor), 0)
        ).filter_by(id_usuario=usuario_id, tipo="despesa").scalar()
    finally:
        session.close()

    total_receitas = float(total_receitas or 0)
    total_despesas = float(total_despesas or 0)
    return total_receitas, total_despesas, total_receitas - total_despesas