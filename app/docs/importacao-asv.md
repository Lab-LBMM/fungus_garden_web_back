# Documentação de Importação de Dados ASV

Este documento apresenta as instruções para importar sequências ASV a partir de arquivos FASTA compactados para o banco de dados MySQL do projeto LBMM.

## 1. Pré-requisitos

Antes de executar a importação, certifique-se de que:

- O ambiente virtual Python está ativo.
- As dependências do projeto foram instaladas.
- O MySQL Server está em execução.
- O arquivo `.env` está configurado corretamente.
- As migrations foram aplicadas ao banco de dados.
- O arquivo `asv_sequences_16S.mod.fasta.gz` está disponível no computador.

Caso ainda não tenha preparado o ambiente, consulte o [README principal](../README.md).

## 2. Script de importação

O script responsável pela importação é:

```text
scripts/import_asv_fasta.py
```

Ele realiza a leitura de registros no formato FASTA dentro de um arquivo `.fasta.gz` e insere as sequências na tabela `asvs`.

Para cada registro, são utilizados os seguintes campos:

| Campo no banco | Origem ou comportamento |
|---|---|
| `unique_identifier` | Cabeçalho do registro FASTA, por exemplo `ASV16S_0001` |
| `marker` | Recebe o valor `16S` |
| `sequence` | Sequência de bases do registro |
| `id` | Gerado automaticamente pelo banco |

## 3. Executar a importação

Execute o script passando o caminho do arquivo FASTA compactado como argumento.

### Git Bash no Windows

```bash
python scripts/import_asv_fasta.py "C:/Users/User/Downloads/asv_sequences_16S.mod.fasta.gz"
```

### PowerShell

```powershell
python scripts/import_asv_fasta.py "C:\Users\User\Downloads\asv_sequences_16S.mod.fasta.gz"
```

Substitua o caminho de exemplo pelo local em que o arquivo está armazenado no seu computador.

## 4. Validações realizadas pelo script

Durante a importação, o script:

- Lê os registros do arquivo FASTA compactado.
- Identifica o cabeçalho de cada registro.
- Extrai as sequências correspondentes.
- Verifica se cada registro possui uma sequência.
- Valida se as sequências utilizam caracteres de bases IUPAC de DNA.
- Insere os registros na tabela `asvs`.

O script utiliza o campo `unique_identifier` para identificar registros já cadastrados.

Dessa forma, pode ser executado novamente sem inserir identificadores que já existem no banco.

## 5. Resultado da importação

Ao finalizar, o script informa a quantidade de sequências inseridas e a quantidade de registros ignorados por já existirem.

## 6. Conferir os dados no MySQL Workbench

Após a importação, conecte-se ao banco do projeto pelo MySQL Workbench.

Para consultar os registros:

```sql
SELECT id, unique_identifier, marker, sequence
FROM asvs
LIMIT 1000;
```

Para verificar a quantidade total:

```sql
SELECT COUNT(*) FROM asvs;
```

Se o MySQL retornar o erro `1046: No database selected`, selecione o schema do projeto ou execute:

```sql
USE nome_do_banco;
```

## 7. Ordem de execução

Para realizar a preparação do banco e a importação dos dados, siga esta ordem:

**1. Aplicar as migrations:**

```bash
python -m alembic upgrade head
```

**2. Importar as sequências ASV:**

```bash
python scripts/import_asv_fasta.py "C:/Users/User/Downloads/asv_sequences_16S.mod.fasta.gz"
```

**3. Iniciar a API:**

```bash
python -m uvicorn app.main:app --reload
```

Com a API iniciada, acesse `http://127.0.0.1:8000/docs` para consultar e testar os endpoints disponíveis. 
