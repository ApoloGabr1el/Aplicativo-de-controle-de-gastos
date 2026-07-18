import customtkinter as ctk
from Funcoes.movimentacoes import listar_movimentacoes, excluir_movimentacao


class tela_historico(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master, fg_color="transparent")
        self.app = app

        self.label_titulo = ctk.CTkLabel(
            self, text="Histórico de Movimentações",
            font=ctk.CTkFont(size=22, weight="bold")
        )
        self.label_titulo.pack(pady=(20, 10))

        self.frame_lista = ctk.CTkScrollableFrame(self, width=500, height=350)
        self.frame_lista.pack(pady=10, padx=20, fill="both", expand=True)

        self.botao_voltar = ctk.CTkButton(
            self, text="Voltar", fg_color="transparent", border_width=2,
            command=lambda: self.app.mostrar_tela("hub")
        )
        self.botao_voltar.pack(pady=(10, 20))

        self.carregar_movimentacoes()

    def carregar_movimentacoes(self):
        for widget in self.frame_lista.winfo_children():
            widget.destroy()

        id_usuario = self.app.usuario_logado[0]
        movimentacoes = listar_movimentacoes(id_usuario)

        if not movimentacoes:
            label_vazio = ctk.CTkLabel(self.frame_lista, text="Nenhuma movimentação registrada ainda.")
            label_vazio.pack(pady=20)
            return

        for id_gasto, tipo, descricao, valor, categoria, data in movimentacoes:
            self.criar_linha(id_gasto, tipo, descricao, valor, categoria, data)

    def criar_linha(self, id_gasto, tipo, descricao, valor, categoria, data):
        linha = ctk.CTkFrame(self.frame_lista)
        linha.pack(fill="x", pady=4, padx=4)

        cor = "#3ba55d" if tipo == "receita" else "#e74c3c"
        sinal = "+" if tipo == "receita" else "-"

        label_info = ctk.CTkLabel(
            linha, text=f"{data}  |  {descricao}  ({categoria})", anchor="w"
        )
        label_info.pack(side="left", padx=10, pady=8, fill="x", expand=True)

        label_valor = ctk.CTkLabel(
            linha, text=f"{sinal} R$ {float(valor):.2f}",
            text_color=cor, font=ctk.CTkFont(weight="bold")
        )
        label_valor.pack(side="left", padx=10)

        botao_excluir = ctk.CTkButton(
            linha, text="Excluir", width=70,
            fg_color="#e74c3c", hover_color="#c0392b",
            command=lambda: self.excluir(id_gasto)
        )
        botao_excluir.pack(side="right", padx=10)

    def excluir(self, id_gasto):
        id_usuario = self.app.usuario_logado[0]
        excluir_movimentacao(id_gasto, id_usuario)
        self.carregar_movimentacoes() 