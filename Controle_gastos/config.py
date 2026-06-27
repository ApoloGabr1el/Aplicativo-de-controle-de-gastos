from dotenv import load_dotenv
import os

load_dotenv()

DB_host = os.getenv ("DB_HOST")
DB_user = os.getenv ("DB_USER")
DB_senha = os.getenv ("DB_PASSWORD")
DB_nome = os.getenv ('DB_NAME')

aparencia = "dark"
cor_tema = "blue"

largura_janela = 900
altura_janela = 600