import customtkinter as ctk
from datetime import date
from Funcoes.movimentacoes import registrar_movimentacao

CATEGORIAS_PADRAO = [
    "Salário", "Freelance", "Investimentos", "Presente", "Outros"
]

class tela_receita(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master, fg_color="transparent")
        self.app = app

        self.label_titulo = ctk.CTkLabel(
            self, text="Nova Receita", font=ctk.CTkFont(size=22, weight="bold")
        )
        self.label_titulo.pack(pady=(40, 20))

        self.label_descricao = ctk.CTkLabel(self, text="Descrição:")
        self.label_descricao.pack(pady=(5, 0))
        self.entry_descricao = ctk.CTkEntry(self, width=280, placeholder_text="Ex: Salário do mês")
        self.entry_descricao.pack()

        self.label_valor = ctk.CTkLabel(self, text="Valor (R$):")
        self.label_valor.pack(pady=(15, 0))
        self.entry_valor = ctk.CTkEntry(self, width=280, placeholder_text="Ex: 2500.00")
        self.entry_valor.pack()

        self.label_categoria = ctk.CTkLabel(self, text="Categoria:")
        self.label_categoria.pack(pady=(15, 0))
        self.combo_categoria = ctk.CTkComboBox(self, width=280, values=CATEGORIAS_PADRAO)
        self.combo_categoria.set("")
        self.combo_categoria.pack()

        self.label_data = ctk.CTkLabel(self, text="Data (AAAA-MM-DD):")
        self.label_data.pack(pady=(15, 0))
        self.entry_data = ctk.CTkEntry(self, width=280)
        self.entry_data.insert(0, date.today().isoformat())
        self.entry_data.pack()

        self.botao_salvar = ctk.CTkButton(self, text="Salvar Receita", command=self.salvar)
        self.botao_salvar.pack(pady=(25, 8))

        self.label_status = ctk.CTkLabel(self, text="")
        self.label_status.pack()

        self.botao_voltar = ctk.CTkButton(
            self, text="Voltar", fg_color="transparent", border_width=2,
            command=lambda: self.app.mostrar_tela("hub")
        )
        self.botao_voltar.pack(pady=(20, 0))

    def salvar(self):
        id_usuario = self.app.usuario_logado[0]
        descricao = self.entry_descricao.get()
        valor = self.entry_valor.get()
        categoria = self.combo_categoria.get()
        data = self.entry_data.get()

        sucesso, mensagem = registrar_movimentacao(
            id_usuario, "receita", descricao, valor, categoria, data
        )

        if sucesso:
            self.label_status.configure(text=mensagem, text_color="green")
            self.entry_descricao.delete(0, "end")
            self.entry_valor.delete(0, "end")
            self.combo_categoria.set("")
        else:
            self.label_status.configure(text=mensagem, text_color="red")