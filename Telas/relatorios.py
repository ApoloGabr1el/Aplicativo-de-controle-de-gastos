import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Funcoes.relatorio import gastos_por_categoria
from Funcoes.graficos import grafico_pizza_categorias, cor_fundo_tema


class tela_relatorios(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master, fg_color="transparent")
        self.app = app

        self.label_titulo = ctk.CTkLabel(
            self, text="Relatório de Despesas por Categoria",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.label_titulo.pack(pady=(20, 10))

        id_usuario = self.app.usuario_logado[0]
        dados = gastos_por_categoria(id_usuario)

        bg_hex = cor_fundo_tema(self)  # self é um widget Tkinter válido aqui
        cor_texto = "white" if ctk.get_appearance_mode() == "Dark" else "black"
        figura = grafico_pizza_categorias(dados, cor_fundo=bg_hex, cor_texto=cor_texto)

        canvas = FigureCanvasTkAgg(figura, master=self)
        canvas.draw()
        canvas.get_tk_widget().configure(bg=bg_hex, highlightthickness=0)
        canvas.get_tk_widget().pack(pady=10)

        self.botao_voltar = ctk.CTkButton(
            self, text="Voltar", fg_color="transparent", border_width=2,
            command=lambda: self.app.mostrar_tela("hub")
        )
        self.botao_voltar.pack(pady=(10, 20))