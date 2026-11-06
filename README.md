# fungus_garden_web_back

Backend da API do projeto LBMM, feito com FastAPI, SQLAlchemy, Alembic e MySQL.

Este guia explica como preparar o ambiente, criar/atualizar as tabelas, importar as sequências ASV do FASTA e testar a API.

## 1. Pré-requisitos

- Python instalado (o ambiente deste projeto foi preparado com Python 3.14).
- MySQL Server instalado e em execução.
- Um banco MySQL criado para o projeto.
- O arquivo `asv_sequences_16S.mod.fasta.gz` disponível no computador para a importação.

Abra o terminal na pasta raiz do projeto, onde ficam `requirements.txt`, `alembic.ini` e a pasta `app`.

## 2. Criar e ativar o ambiente Python

Faça esta etapa apenas se ainda não existir a pasta `venv`.

### PowerShell

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação por política de execução, abra o terminal Git Bash ou use a ativação apropriada à política já configurada na sua máquina.

### Git Bash no Windows

```bash
python -m venv venv
source venv/Scripts/activate
```

### Linux ou macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Quando o ambiente estiver ativo, o terminal normalmente mostra `(venv)` no início da linha.

## 3. Instalar as dependências

Com o ambiente virtual ativo:

```bash
python -m pip install -r requirements.txt
```

## 4. Configurar a conexão com o MySQL

Crie ou edite o arquivo `.env` na raiz do projeto. Informe a URL de conexão e substitua os valores de exemplo pelos seus:

```env
DATABASE_URL=mysql+pymysql://usuario:senha@localhost:3306/nome_do_banco?charset=utf8mb4
```

O banco indicado em `nome_do_banco` precisa existir no MySQL antes de executar as migrations. Se a senha tiver caracteres especiais, eles precisam estar codificados para uso em uma URL. Não compartilhe nem envie o arquivo `.env` para o repositório.

## 5. Criar ou atualizar as tabelas

Com o ambiente ativo e o `.env` configurado, rode na raiz do projeto:

```bash
python -m alembic upgrade head
```

Esse comando aplica as migrations pendentes até a versão mais recente. Ele cria as tabelas definidas pelas migrations, incluindo `asvs`. O comando não importa os registros do FASTA; isso é feito na etapa seguinte.

Se o comando terminar sem erro, as migrations foram aplicadas. Se houver erro de conexão, confira se o MySQL está em execução, se o nome do banco existe e se a `DATABASE_URL` está correta.

## 6. Importar sequências ASV do FASTA compactado

O script `scripts/import_asv_fasta.py` lê registros no formato FASTA dentro de um arquivo `.fasta.gz`. Para cada registro:

- o cabeçalho, como `ASV16S_0001`, vira `unique_identifier` (identificador do laboratório);
- `marker` recebe o valor `16S`;
- as bases são gravadas em `sequence`;
- o `id` é gerado automaticamente pelo banco.

Execute o script passando o caminho do arquivo como argumento. No Git Bash, por exemplo:

```bash
python scripts/import_asv_fasta.py "C:/Users/User/Downloads/asv_sequences_16S.mod.fasta.gz"
```

No PowerShell, o mesmo comando funciona com o caminho do Windows:

```powershell
python scripts/import_asv_fasta.py "C:\Users\User\Downloads\asv_sequences_16S.mod.fasta.gz"
```

Uma execução concluída mostra quantas sequências foram inseridas e quantas foram ignoradas por já existirem. O script compara pelo `unique_identifier`, então pode ser executado novamente sem inserir de novo os identificadores já cadastrados. Ele valida que cada registro tenha sequência e que use caracteres de bases IUPAC de DNA.

## 7. Conferir os registros no MySQL Workbench

No Workbench, conecte ao servidor e dê dois cliques no banco do projeto na lista **SCHEMAS** à esquerda para selecioná-lo. Depois execute:

```sql
SELECT id, unique_identifier, marker, sequence
FROM asvs
LIMIT 1000;
```

Para verificar quantos registros existem:

```sql
SELECT COUNT(*) FROM asvs;
```

O banco selecionado aparece em negrito na lista **SCHEMAS**. Se o MySQL retornar o erro `1046: No database selected`, selecione o schema ou execute `USE nome_do_banco;` antes da consulta.

## 8. Iniciar e testar a API

Abra um terminal com o ambiente virtual ativo e inicie a aplicação na raiz do projeto:

```bash
python -m uvicorn app.main:app --reload
```

Deixe esse terminal aberto enquanto testa a API. Acesse no navegador:

- `http://127.0.0.1:8000/` — deve retornar a mensagem `LBMM API funcionando!`.
- `http://127.0.0.1:8000/test-database` — deve retornar o nome do banco conectado.
- `http://127.0.0.1:8000/docs` — documentação interativa do Swagger, onde você pode executar os endpoints disponíveis.

Por exemplo, na documentação Swagger, procure `GET /organisms/count` e clique em **Try it out** e **Execute**. A resposta esperada contém a quantidade de organismos.

Para parar a API, volte ao terminal em que o Uvicorn está rodando e pressione `Ctrl+C`.

## 9. Ordem resumida para uso normal

Em um terminal novo, ative o ambiente virtual e rode os comandos nesta ordem:

```bash
python -m alembic upgrade head
python scripts/import_asv_fasta.py "C:/Users/User/Downloads/asv_sequences_16S.mod.fasta.gz"
python -m uvicorn app.main:app --reload
```

O primeiro atualiza o schema, o segundo importa os ASVs e o terceiro inicia a API. Para conferir a API, abra `http://127.0.0.1:8000/docs`.
