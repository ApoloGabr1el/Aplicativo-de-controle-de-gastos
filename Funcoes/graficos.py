import customtkinter as ctk
import matplotlib.pyplot as plt


def cor_fundo_tema(widget):
    modo = ctk.get_appearance_mode()  
    cores = ctk.ThemeManager.theme["CTkFrame"]["fg_color"]
    cor = cores[1] if modo == "Dark" else cores[0]

    r, g, b = widget.winfo_rgb(cor)
    return f"#{r // 256:02x}{g // 256:02x}{b // 256:02x}"


def grafico_pizza_categorias(dados: dict, cor_fundo="#242424", cor_texto="white"):
    fig, ax = plt.subplots(figsize=(5, 4))
    fig.patch.set_facecolor(cor_fundo)
    ax.set_facecolor(cor_fundo)

    if not dados:
        ax.text(0.5, 0.5, "Nenhuma despesa registrada", ha="center", va="center", color=cor_texto)
        ax.axis("off")
        return fig

    categorias = list(dados.keys())
    valores = list(dados.values())

    ax.pie(
        valores, labels=categorias, autopct="%1.1f%%", startangle=90,
        textprops={"color": cor_texto}
    )
    ax.set_title("Despesas por Categoria", color=cor_texto)
    ax.axis("equal")

    return fig