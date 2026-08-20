# Aplicativo de Controle de Gastos

Aplicativo desenvolvido em **Python** para auxiliar no controle e organização de gastos pessoais. O projeto permite registrar, consultar e gerenciar informações financeiras por meio de uma interface gráfica integrada a um banco de dados.

> Projeto desenvolvido com o objetivo de praticar **Python, desenvolvimento de interfaces, banco de dados e organização de aplicações**.

## Funcionalidades

*  Cadastro de gastos
*  Visualização dos gastos registrados
*  Gerenciamento das informações
*  Integração com banco de dados MySQL
*  Interface gráfica
*  Configuração do banco de dados através de variáveis de ambiente

## Tecnologias utilizadas

* **Python**
* **MySQL**
* **Tkinter**
* **python-dotenv**
* **Git/GitHub**

##  Estrutura do projeto

```text
Aplicativo-de-controle-de-gastos/
│
├── Controle_gastos/
│   ├── Funcoes/
│   ├── Telas/
│   ├── banco.py
│   ├── config.py
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
```

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/ApoloGabr1el/Aplicativo-de-controle-de-gastos.git
```

Entre na pasta:

```bash
cd Aplicativo-de-controle-de-gastos
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente virtual.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Crie um banco de dados MySQL e configure as informações de conexão no arquivo `.env`.

Exemplo:

```env
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=seu_banco
```

 Não compartilhe suas credenciais do banco de dados. O arquivo `.env` deve permanecer fora do controle de versão.

### 5. Execute o aplicativo

```bash
python run.py
```


## O que aprendi com este projeto

Durante o desenvolvimento, pude praticar conceitos importantes de desenvolvimento de software, como:

* Organização de projetos Python
* Programação modular
* Criação de interfaces gráficas
* Conexão entre Python e MySQL
* Operações com banco de dados
* Gerenciamento de dependências
* Uso de variáveis de ambiente
* Organização e versionamento com Git


##  Autor

**ApoloGabr1el**

Estudante de **Informática para Internet** interessado em desenvolvimento de software, Python e tecnologias relacionadas a back-end.

📌 GitHub: [ApoloGabr1el](https://github.com/ApoloGabr1el)

---

⭐ Se este projeto foi útil ou interessante para você, considere deixar uma estrela no repositório!
