# Aplicativo-de-controle-de-gastos

## Passo a passo

### 1. Clone o repositório


### 2. Instale as dependências

```bash
py -m pip install -r Controle_gastos/requirements.txt
```

### 3. Configure o banco de dados

Abra o MySQL Workbench ou o terminal do MySQL e execute:

```sql
CREATE DATABASE db_controle_gastos;
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` dentro da pasta `Controle_gastos/` com base no modelo abaixo:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=db_controle_gastos
```