import mysql.connector
from Controle_gastos.config import DB_host, DB_nome, DB_senha, DB_user

def conectar():
    return mysql.connector.connect(
        host = DB_host,
        user = DB_user,
        password = DB_senha,
        database = DB_nome
    )
def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(""" create table if not exists usuarios(
                   id int auto_increment primary key,
                   nome varchar(100) not null,
                   email varchar(100) unique not null,
                   senha varchar (255) not null
                   )
    """)
    cursor.execute(
        """ create table if not exists gastos(
        id int auto_increment primary key,
        id_usuario int,
        tipo varchar (20) not null,
        descricao varchar(255) not null,
        valor decimal (10, 2) not null,
        categoria varchar(50) not null,
        data date not null,

        foreign key (id_usuario)
        references usuarios(id))
        """
    )

    conn.commit()
    conn.close()