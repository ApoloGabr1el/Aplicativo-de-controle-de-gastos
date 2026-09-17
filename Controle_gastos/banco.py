from urllib.parse import quote_plus

from sqlalchemy import DECIMAL, Date, Column, ForeignKey, Integer, String, create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from Controle_gastos.config import DB_host, DB_nome, DB_senha, DB_user


class Base(DeclarativeBase):
    pass


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)


class Gasto(Base):
    __tablename__ = "gastos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    tipo = Column(String(20), nullable=False)
    descricao = Column(String(255), nullable=False)
    valor = Column(DECIMAL(10, 2), nullable=False)
    categoria = Column(String(50), nullable=False)
    data = Column(Date, nullable=False)


DATABASE_URL = (
    f"mysql+pymysql://{DB_user}:{quote_plus(DB_senha)}@"
    f"{DB_host}/{DB_nome}?charset=utf8mb4"
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)


def conectar():
    return Session()


def criar_banco():
    url_sem_banco = f"mysql+pymysql://{DB_user}:{quote_plus(DB_senha)}@{DB_host}/?charset=utf8mb4"
    engine_servidor = create_engine(url_sem_banco, pool_pre_ping=True)
    nome_seguro = DB_nome.replace("`", "")
    try:
        with engine_servidor.begin() as conn:
            conn.execute(text(
                f"CREATE DATABASE IF NOT EXISTS `{nome_seguro}` "
                "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
            ))
    finally:
        engine_servidor.dispose()


def criar_tabelas():
    criar_banco()
    Base.metadata.create_all(engine)