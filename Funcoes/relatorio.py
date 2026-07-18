from Funcoes.movimentacoes import listar_movimentacoes


def gastos_por_categoria(usuario_id):
    movimentacoes = listar_movimentacoes(usuario_id, tipo="despesa")

    totais = {}
    for _, tipo, descricao, valor, categoria, data in movimentacoes:
        valor = float(valor)
        totais[categoria] = totais.get(categoria, 0) + valor

    return totais