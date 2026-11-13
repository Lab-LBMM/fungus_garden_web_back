fungus_garden_web_back

Backend da API do projeto LBMM, desenvolvido com FastAPI, SQLAlchemy, Alembic e MySQL.

Este guia apresenta as instruções para preparar o ambiente, configurar o banco de dados, executar as migrations e iniciar a API.

 1. Pré-requisitos
- Python instalado (o ambiente deste projeto foi preparado com Python 3.14).
- MySQL Server instalado e em execução.
- Um banco MySQL criado para o projeto.

Abra o terminal na pasta raiz do projeto, onde ficam `requirements.txt`, `alembic.ini` e a pasta `app`.

2. Criar e ativar o ambiente Python
Faça esta etapa apenas se ainda não existir a pasta `venv`.
PowerShell
```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação por política de execução, utilize o Git Bash ou configure a política de execução apropriada.
Git Bash no Windows

```bash
python -m venv venv
source venv/Scripts/activate
```

Linux ou macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

Quando o ambiente estiver ativo, o terminal normalmente mostra `(venv)` no início da linha.

 3. Instalar as dependências
Com o ambiente virtual ativo:
```bash
python -m pip install -r requirements.txt
```
4. Configurar a conexão com o MySQL
Crie ou edite o arquivo `.env` na raiz do projeto. Informe a URL de conexão, substituindo os valores de exemplo:
```env
DATABASE_URL=mysql+pymysql://usuario:senha@localhost:3306/nome_do_banco?charset=utf8mb4
```
O banco indicado em `nome_do_banco` precisa existir no MySQL antes de executar as migrations.
Se a senha tiver caracteres especiais, eles precisam ser codificados para uso em uma URL.
**Importante:** não compartilhe nem envie o arquivo `.env` para o repositório.

 5. Criar ou atualizar as tabelas
Com o ambiente ativo e o `.env` configurado, execute na raiz do projeto:
```bash
python -m alembic upgrade head
```
Esse comando aplica as migrations pendentes até a versão mais recente, criando ou atualizando as tabelas definidas nas migrations, incluindo `asvs`.
O comando não importa os registros do FASTA.
Se houver erro de conexão, confira se o MySQL está em execução, se o banco existe e se a `DATABASE_URL` está correta.

6. Importação de dados
As instruções para importação de sequências ASV e utilização dos scripts de inserção de dados estão disponíveis na documentação específica:
[Documentação de importação de dados (docs/importacao-asv.md)](docs/importacao-asv.md)

7. Iniciar e testar a API
Abra um terminal com o ambiente virtual ativo e inicie a aplicação na raiz do projeto:
```bash
python -m uvicorn app.main:app --reload
```
Deixe esse terminal aberto enquanto testa a API.
Acesse no navegador:
- `http://127.0.0.1:8000/` — retorna a mensagem de funcionamento da API.
- `http://127.0.0.1:8000/test-database` — retorna o nome do banco conectado.
- `http://127.0.0.1:8000/docs` — documentação interativa do Swagger, onde é possível executar os endpoints disponíveis.

Para parar a API, volte ao terminal em que o Uvicorn está rodando e pressione `Ctrl+C`.
