import logging
import os
from typing import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine, event, text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

load_dotenv()

logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────────────────────────────────────
# Validação da DATABASE_URL
# ─────────────────────────────────────────────────────────────────────────────

DATABASE_URL: str = os.getenv("DATABASE_URL", "")

if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL não está definida. "
        "Verifique o arquivo .env na raiz do projeto.\n"
        "Formato esperado: mysql+pymysql://usuario:senha@host:porta/banco"
    )

# ─────────────────────────────────────────────────────────────────────────────
# Pool de conexões configurável via variáveis de ambiente
# ─────────────────────────────────────────────────────────────────────────────

_POOL_SIZE    = int(os.getenv("DB_POOL_SIZE",    "5"))
_MAX_OVERFLOW = int(os.getenv("DB_MAX_OVERFLOW", "10"))
_POOL_TIMEOUT = int(os.getenv("DB_POOL_TIMEOUT", "30"))
_POOL_RECYCLE = int(os.getenv("DB_POOL_RECYCLE", "1800"))  # 30 min

engine = create_engine(
    DATABASE_URL,
    echo=os.getenv("DB_ECHO", "false").lower() == "true",
    pool_size=_POOL_SIZE,
    max_overflow=_MAX_OVERFLOW,
    pool_timeout=_POOL_TIMEOUT,
    pool_recycle=_POOL_RECYCLE,
    pool_pre_ping=True,   # verifica conexão antes de usar (reconecta se caiu)
)

# ─────────────────────────────────────────────────────────────────────────────
# Sessão
# ─────────────────────────────────────────────────────────────────────────────

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# ─────────────────────────────────────────────────────────────────────────────
# Base declarativa — todas as models herdam desta classe
# ─────────────────────────────────────────────────────────────────────────────

class Base(DeclarativeBase):
    pass


# ─────────────────────────────────────────────────────────────────────────────
# Dependency injection para FastAPI (usar com Depends)
# ─────────────────────────────────────────────────────────────────────────────

def get_db() -> Generator[Session, None, None]:
    """
    Provê uma sessão de banco de dados por requisição HTTP.

    Uso:
        @app.get("/exemplo")
        def rota(db: Session = Depends(get_db)):
            ...
    """
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as exc:
        logger.error("Erro na sessão de banco de dados: %s", exc)
        db.rollback()
        raise
    finally:
        db.close()
