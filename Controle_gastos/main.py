import customtkinter as ctk
from Controle_gastos.config import altura_janela, largura_janela
from Telas.Inicio import tela_inicio
from Telas.Login import tela_login
from Telas.Cadastro import tela_cadastro
from Telas.hub import tela_hub
from Telas.despesa import tela_despesa
from Telas.receita import tela_receita
from Telas.relatorios import tela_relatorios
from Telas.historico import tela_historico

TELAS = {
    "inicio": tela_inicio,
    "login": tela_login,
    "cadastro": tela_cadastro,
    "hub": tela_hub,
    "despesa": tela_despesa,
    "receita": tela_receita,
    "relatorios": tela_relatorios,
    "historico": tela_historico
}

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Controle de Gastos")
        self.geometry(f"{largura_janela}x{altura_janela}")

        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True)

        self.usuario_logado = None  
        self.tela_atual = None

        self.mostrar_tela("inicio")

    def mostrar_tela(self, nome, **kwargs):
        if self.tela_atual is not None:
            self.tela_atual.destroy()

        classe = TELAS[nome]
        self.tela_atual = classe(self.container, self, **kwargs)
        self.tela_atual.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()