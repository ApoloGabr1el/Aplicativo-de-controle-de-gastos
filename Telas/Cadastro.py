import customtkinter as ctk
from Funcoes.usuario import cadastrar_usuario

class tela_cadastro(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master, fg_color="transparent")
        self.app = app

        self.label_nome = ctk.CTkLabel(self, text="Nome:")
        self.label_nome.pack(pady=(60, 5))

        self.entry_nome = ctk.CTkEntry(self, width=250, placeholder_text="Seu nome completo")
        self.entry_nome.pack()

        self.label_email = ctk.CTkLabel(self, text="Email:")
        self.label_email.pack(pady=(20, 5))

        self.entry_email = ctk.CTkEntry(self, width=250, placeholder_text='seuemail@exemplo.com')
        self.entry_email.pack()

        self.label_senha = ctk.CTkLabel(self, text="Senha:")
        self.label_senha.pack(pady=(20, 5))

        self.entry_senha = ctk.CTkEntry(self, width=250, placeholder_text="Sua senha", show="*")
        self.entry_senha.pack()

        self.label_confirmar_senha = ctk.CTkLabel(self, text="Confirmar senha:")
        self.label_confirmar_senha.pack(pady=(20, 5))

        self.entry_confirmar_senha = ctk.CTkEntry(self, width=250, placeholder_text="Repita sua senha", show="*")
        self.entry_confirmar_senha.pack()

        self.botao_cadastrar = ctk.CTkButton(self, text="Cadastrar", command=self.fazer_cadastro)
        self.botao_cadastrar.pack(pady=(30))

        self.label_erro = ctk.CTkLabel(self, text="")
        self.label_erro.pack()

        self.botao_voltar = ctk.CTkButton(
            self, text="Voltar", fg_color="transparent",border_width=2,
            command=lambda: self.app.mostrar_tela("inicio")
        )
        self.botao_voltar.pack(pady=(15, 0))

    def fazer_cadastro(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        confirmar_senha = self.entry_confirmar_senha.get()

        if senha != confirmar_senha:
            self.label_erro.configure(text="As senhas não coincidem", text_color="red")
            return

        if len(senha) < 6:
            self.label_erro.configure(text="A senha deve ter no mínimo 6 caracteres", text_color="red")
            return

        sucesso, mensagem = cadastrar_usuario(nome, email, senha)

        if sucesso:
            self.label_erro.configure(text=f"{mensagem} Redirecionando para o login...", text_color="green")
            self.after(1500, lambda: self.app.mostrar_tela("login"))
        else:
            self.label_erro.configure(text=mensagem, text_color="red")