import customtkinter as ctk
from Funcoes.usuario import validar_login
from Controle_gastos.config import altura_janela, largura_janela

class tela_login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login - Controle de Gastos")
        self.geometry (f"{largura_janela}x{altura_janela}")

        self.label_email = ctk.CTkLabel(self, text="Email:")
        self.label_email.pack(pady=(150, 5))

        self.entry_email = ctk.CTkEntry(self, width=250, placeholder_text='seuemail@exemplo.com')
        self.entry_email.pack()

        self.label_senha = ctk.CTkLabel(self, text="Senha:")
        self.label_senha.pack (pady=(30, 5))

        self.entry_senha = ctk.CTkEntry(self, width=250, placeholder_text="Sua senha", show="*")
        self.entry_senha.pack()

        self.botao_login = ctk.CTkButton(self, text="Entrar", command=self.fazer_login)
        self.botao_login.pack(pady=(30))

        self.label_erro = ctk.CTkLabel (self, text="")
        self.label_erro.pack()
    
    def fazer_login(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        usuario = validar_login(email, senha)

        if usuario:
            self.label_erro.configure(text="Login realizado com sucesso!", text_color= "green")
            print("Usuario logado", usuario)
        else:
            self.label_erro.configure(text="Email ou Senha incorretos", text_color = "red")

if __name__ == "__main__":
    app = tela_login()
    app.mainloop()