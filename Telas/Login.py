import customtkinter as ctk
from Funcoes.usuario import validar_login

class tela_login(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master, fg_color="transparent")
        self.app = app

        self.label_email = ctk.CTkLabel(self, text="Email:")
        self.label_email.pack(pady=(150, 5))

        self.entry_email = ctk.CTkEntry(self, width=250, placeholder_text='seuemail@exemplo.com')
        self.entry_email.pack()

        self.label_senha = ctk.CTkLabel(self, text="Senha:")
        self.label_senha.pack(pady=(30, 5))

        self.entry_senha = ctk.CTkEntry(self, width=250, placeholder_text="Sua senha", show="*")
        self.entry_senha.pack()

        self.botao_login = ctk.CTkButton(self, text="Entrar", command=self.fazer_login)
        self.botao_login.pack(pady=(30))

        self.label_erro = ctk.CTkLabel(self, text="")
        self.label_erro.pack()

        self.botao_voltar = ctk.CTkButton(
            self, text="Voltar", fg_color="transparent", border_width=2,
            command=lambda: self.app.mostrar_tela("inicio")
        )
        self.botao_voltar.pack(pady=(20, 0))

    def fazer_login(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        usuario = validar_login(email, senha)

        if usuario:
            self.app.usuario_logado = usuario
            self.app.mostrar_tela("hub")
        else:
            self.label_erro.configure(text="Email ou senha incorretos", text_color= "red")