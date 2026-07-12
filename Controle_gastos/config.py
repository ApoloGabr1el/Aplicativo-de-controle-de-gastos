from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(dotenv_path)

DB_host = os.getenv ("DB_HOST")
DB_user = os.getenv ("DB_USER")
DB_senha = os.getenv ("DB_PASSWORD")
DB_nome = os.getenv ('DB_NAME')

aparencia = "dark"
cor_tema = "blue"

largura_janela = 900
altura_janela = 600