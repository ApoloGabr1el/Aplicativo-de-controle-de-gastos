import customtkinter as ctk

class tela_inicio(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master, fg_color="transparent")
        self.app = app

        self.label_titulo = ctk.CTkLabel(
            self, text="Controle de Gastos",
            font=ctk.CTkFont(size=26, weight="bold")
        )
        self.label_titulo.pack(pady=(150, 10))

        self.label_subtitulo = ctk.CTkLabel(
            self, text="Organize suas finanças com simplicidade",
            font=ctk.CTkFont(size=14)
        )
        self.label_subtitulo.pack(pady=(0, 40))

        self.botao_entrar = ctk.CTkButton(
            self, text="Entrar", width=250,
            command=lambda: self.app.mostrar_tela("login")
        )
        self.botao_entrar.pack(pady=10)

        self.botao_cadastrar = ctk.CTkButton(
            self, text="Criar conta", width=250,
            fg_color="transparent", border_width=2,
            command=lambda: self.app.mostrar_tela("cadastro")
        )
        self.botao_cadastrar.pack(pady=10)