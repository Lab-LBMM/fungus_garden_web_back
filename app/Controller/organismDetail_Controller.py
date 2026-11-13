from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.Service.organismDetail_Service import buscar_descricao

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/organisms/{organism_id}/description")
def get_descricao(
    organism_id: int,
    db: Session = Depends(get_db)
):
    descricao = buscar_descricao(db, organism_id)

    if descricao is None:
        raise HTTPException(
            status_code=404,
            detail="Descrição do organismo não encontrada"
        )

    return {
        "organism_id": organism_id,
        "description": descricao
    }