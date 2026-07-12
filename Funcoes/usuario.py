import mysql.connector
from Controle_gastos.banco import conectar
import hashlib

def senha_segura(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def validar_login(email, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "select * from usuarios where email = %s and senha = %s",
        (email, senha_segura(senha))
    )
    usuario = cursor.fetchone()

    conn.close()
    return usuario 

def cadastrar_usuario(nome, email, senha):
    if not nome or not email or not senha:
        return False, "Preencha todos os campos"
    
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("select id from usuarios where email = %s", (email,))
    if cursor.fetchone():
        conn.close()
        return False, "este email já está cadastrado."

    senha_criptografada = senha_segura(senha)

    try:
        cursor.execute("insert into usuarios(nome, email, senha) values (%s, %s, %s)", (nome, email, senha_criptografada))
        conn.commit()
        return True, "Usuario Cadastrado com sucesso!"
    except mysql.connector.Error as erro:
        conn.rollback()
        return False, f"Erro ao cadastrar: {erro}"
    finally:
        conn.close()