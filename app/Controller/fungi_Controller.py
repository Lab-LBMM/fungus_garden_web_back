
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.Service.fungi_Service import (
    buscar_pagina_fungo,
    buscar_descricao_fungo,
    buscar_caracteristicas_fungo
)

router = APIRouter(prefix="/fungi", tags=["Fungi"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{organism_id}")
def obter_pagina_fungo(
    organism_id: int,
    db: Session = Depends(get_db)
):
    resultado = buscar_pagina_fungo(db, organism_id)

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Fungo não encontrado."
        )

    return resultado


@router.get("/{organism_id}/description")
def obter_descricao_fungo(
    organism_id: int,
    db: Session = Depends(get_db)
):
    resultado = buscar_descricao_fungo(db, organism_id)

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Fungo não encontrado."
        )

    return resultado


@router.get("/{organism_id}/characteristics")
def obter_caracteristicas_fungo(
    organism_id: int,
    db: Session = Depends(get_db)
):
    resultado = buscar_caracteristicas_fungo(db, organism_id)

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Fungo não encontrado."
        )

    return resultado
