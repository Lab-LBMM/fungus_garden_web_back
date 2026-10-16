import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# ─────────────────────────────────────────────────────────────────────────────
# Garante que o diretório raiz do projeto está no sys.path para que
# "from app.database import Base" e as models sejam encontradas.
# ─────────────────────────────────────────────────────────────────────────────
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importa o Base e todas as models (necessário para autogenerate detectar tabelas)
from app.database import Base, DATABASE_URL  # noqa: E402
import app.Models  # noqa: F401, E402 — registra todas as 14 models no metadata

# ─────────────────────────────────────────────────────────────────────────────
# Configuração do Alembic
# ─────────────────────────────────────────────────────────────────────────────
config = context.config

# Injeta a DATABASE_URL do .env no config do Alembic (substitui o valor do .ini)
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Configura logging a partir do alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Aponta para o metadata das models — necessário para "alembic revision --autogenerate"
target_metadata = Base.metadata


# ─────────────────────────────────────────────────────────────────────────────
# Execução offline (gera SQL sem conectar ao banco)
# ─────────────────────────────────────────────────────────────────────────────
def run_migrations_offline() -> None:
    """Gera scripts SQL sem abrir conexão real com o banco."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


# ─────────────────────────────────────────────────────────────────────────────
# Execução online (conecta ao banco e aplica as migrações)
# ─────────────────────────────────────────────────────────────────────────────
def run_migrations_online() -> None:
    """Aplica migrações com conexão ativa ao banco."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,         # detecta mudanças de tipo de coluna
            compare_server_default=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
