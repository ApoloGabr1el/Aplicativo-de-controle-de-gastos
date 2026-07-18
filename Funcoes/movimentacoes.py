import mysql.connector
from Controle_gastos.banco import conectar

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
    
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """insert into gastos (usuario_id, tipo, descricao, valor, categoria, data)
               values (%s, %s, %s, %s, %s, %s)""",
            (usuario_id, tipo, descricao, valor, categoria, data)
        )
        conn.commit()
        return True, f"{tipo.capitalize()} registrada com sucesso!"
    except mysql.connector.Error as erro:
        conn.rollback()
        return False, f"Erro ao registrar: {erro}"
    finally:
        conn.close()

def listar_movimentacoes(usuario_id, tipo=None):
    conn = conectar()
    cursor = conn.cursor()

    if tipo:
        cursor.execute(
            """select id, tipo, descricao, valor, categoria, data
               from gastos where usuario_id = %s and tipo = %s
               order by data desc""",
            (usuario_id, tipo)
        )
    else:
        cursor.execute(
            """select id, tipo, descricao, valor, categoria, data
               from gastos where usuario_id = %s
               order by data desc""",
            (usuario_id,)
        )

    resultado = cursor.fetchall()
    conn.close()
    return resultado

def excluir_movimentacao(id_gasto, usuario_id):
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "delete from gastos where id = %s and usuario_id = %s",
            (id_gasto, usuario_id)
        )
        conn.commit()
        if cursor.rowcount == 0:
            return False, "Movimentação não encontrada."
        return True, "Movimentação excluída com sucesso!"
    except mysql.connector.Error as erro:
        conn.rollback()
        return False, f"Erro ao excluir: {erro}"
    finally:
        conn.close()

def calcular_saldo(usuario_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "select coalesce(sum(valor), 0) from gastos where usuario_id = %s and tipo = 'receita'",
        (usuario_id,)
    )
    total_receitas = float(cursor.fetchone()[0])

    cursor.execute(
        "select coalesce(sum(valor), 0) from gastos where usuario_id = %s and tipo = 'despesa'",
        (usuario_id,)
    )
    total_despesas = float(cursor.fetchone()[0])

    conn.close()

    saldo = total_receitas - total_despesas
    return total_receitas, total_despesas, saldo