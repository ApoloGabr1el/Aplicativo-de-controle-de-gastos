import customtkinter as ctk

class tela_hub(ctk.CTkFrame):
    def __init__ (self, master, app):
        super().__init__(master, fg_color="transparent")
        self.app = app

        nome_usuario = self.app.usuario_logado[1] if self.app.usuario_logado else "Usuario"
        self.label_boasvindas = ctk.CTkLabel(self, text=f"Olá {nome_usuario}!", 
                                             font=ctk.CTkFont(size=24, weight="bold"))
        self.label_boasvindas.pack(pady=(60,5))

        self.label_subtitulo = ctk.CTkLabel(
        self, text="O que você quer fazer hoje?", 
        font=ctk.CTkFont(size=14))
        self.label_subtitulo.pack(pady=(0, 40)
        )

        self.botao_despesa = ctk.CTkButton(
            self, text="Nova Despesa", width=250,
            command=lambda: self.app.mostrar_tela("despesa")
        )
        self.botao_despesa.pack(pady=8)

        self.botao_receita = ctk.CTkButton(
            self, text="Nova Receita", width=250,
            command=lambda: self.app.mostrar_tela("receita")
        )
        self.botao_receita.pack(pady=8)

        self.botao_historico = ctk.CTkButton(
            self, text="Histórico", width=250,
            command=lambda: self.app.mostrar_tela("historico")
        )
        self.botao_historico.pack(pady=8)

        self.botao_relatorios = ctk.CTkButton(
            self, text="Relatórios", width=250,
            command=lambda: self.app.mostrar_tela("relatorios")
        )
        self.botao_relatorios.pack(pady=8)

        self.botao_sair = ctk.CTkButton(
            self, text="Sair", width=250,
            fg_color="transparent", border_width=2,
            command=self.sair
        )
        self.botao_sair.pack(pady=(30, 8))

    def sair(self):
        self.app.usuario_logado = None
        self.app.mostrar_tela("inicio")