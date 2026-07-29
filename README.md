# Fungus Garden Web - Backend API

API RESTful backend desenvolvida para o gerenciamento, armazenamento e consulta de dados biológicos e genômicos de formigas, fungos, bactérias e sequências genéticas do projeto **Fungus Garden** (UNESP).

---

## Tecnologias Utilizadas

- **[Python 3.10+](https://www.python.org/)** — Linguagem de programação principal.
- **[FastAPI](https://fastapi.tiangolo.com/)** — Framework web assíncrono de alto desempenho para construção de APIs.
- **[SQLAlchemy 2.0](https://www.sqlalchemy.org/)** — ORM (Object-Relational Mapping) para modelagem e manipulação de dados.
- **[MySQL](https://www.mysql.com/)** — Sistema de Gerenciamento de Banco de Dados Relacional (SGBD).
- **[PyMySQL](https://pymysql.readthedocs.io/)** — Driver de conexão Python puro para o MySQL.
- **[Alembic](https://alembic.sqlalchemy.org/)** — Ferramenta de migração e versionamento de esquema do banco de dados.
- **[Uvicorn](https://www.uvicorn.org/)** — Servidor ASGI leve e rápido para execução da aplicação FastAPI.
- **[Pydantic](https://docs.pydantic.dev/)** — Validação e parsing de dados com tipagem estática.
- **[python-dotenv](https://github.com/theskumar/python-dotenv)** — Gerenciamento de variáveis de ambiente via arquivo `.env`.

---

## Pré-requisitos

Antes de iniciar, certifique-se de ter instalado em sua máquina:

1. **Python 3.10** ou superior.
2. **MySQL Server** (rodando localmente ou via container Docker).
3. **Git** para clonar o repositório.

---

## Como Rodar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/Lab-LBMM/fungus_garden_web_back.git
cd fungus_garden_web_back
```

### 2. Criar e ativar o ambiente virtual (`venv`)

- **No Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```

- **No Linux ou macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar as Variáveis de Ambiente (`.env`)
Crie um arquivo `.env` na raiz do projeto contendo a URL de conexão com o seu banco MySQL:

```env
DATABASE_URL=mysql+pymysql://seu_usuario:sua_senha@localhost:3306/fungus_garden_db
```

> **Substitua:**
> - `seu_usuario`: Seu usuário do MySQL (ex: `root`).
> - `sua_senha`: Sua senha do MySQL.
> - `localhost:3306`: Host e porta do MySQL.
> - `fungus_garden_db`: Nome da base de dados.

### 5. Criar o Banco de Dados no MySQL
Abra seu cliente MySQL (MySQL Workbench, DBeaver ou Terminal) e crie a base de dados:

```sql
CREATE DATABASE fungus_garden_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 6. Executar as Migrações do Banco de Dados (Alembic)

Gere a migração inicial e aplique o esquema das tabelas no MySQL:

```bash
# 1. Gerar o arquivo de migração inicial com base nos models
alembic revision --autogenerate -m "Criacao inicial das tabelas"

# 2. Aplicar a migração no banco MySQL
alembic upgrade head
```

### 7. Iniciar o Servidor de Desenvolvimento
Rode a aplicação com o **Uvicorn**:

```bash
uvicorn app.main:app --reload
```

A API estará disponível em: `http://127.0.0.1:8000`

---

## Documentação Interativa (Swagger & ReDoc)

Com o servidor rodando, você pode acessar a documentação automática gerada pelo FastAPI nos seguintes links:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

---

## Estrutura do Projeto

```text
fungus_garden_web_back/
├── alembic/              # Configurações e scripts de migração do banco
│   ├── versions/         # Histórico de arquivos de migração
│   └── env.py            # Script de ambiente do Alembic
├── app/
│   ├── controllers/      # Controladores / Endpoints das rotas da API
│   ├── core/             # Configurações centrais da aplicação
│   ├── models/           # Entidades e mapeamento SQLAlchemy
│   ├── repositories/     # Camada de acesso a dados (Queries)
│   ├── schemas/          # Modelos Pydantic (Request/Response)
│   ├── services/         # Regras de negócio da aplicação
│   ├── database.py       # Configuração da conexão com a base de dados
│   └── main.py           # Ponto de entrada da aplicação FastAPI
├── .env                  # Variáveis de ambiente (não commitado)
├── alembic.ini           # Configuração global do Alembic
├── requirements.txt      # Dependências do projeto Python
└── README.md             # Documentação do projeto
```