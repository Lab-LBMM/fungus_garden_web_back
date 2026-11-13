
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.Service.ant_Service import (
    buscar_descricao_formiga,
    buscar_caracteristicas_formiga,
    buscar_pagina_formiga, 
    buscar_fungos_da_formiga
)

router = APIRouter(
    prefix="/ants",
    tags=["Ants"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{organism_id}/description")
def obter_descricao(
    organism_id: int,
    db: Session = Depends(get_db)
):
    resultado = buscar_descricao_formiga(db, organism_id)

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Formiga não encontrada."
        )

    return resultado


@router.get("/{organism_id}/ecology")
def obter_caracteristicas(
    organism_id: int,
    db: Session = Depends(get_db)
):
    resultado = buscar_caracteristicas_formiga(db, organism_id)

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Formiga não encontrada."
        )

    return resultado


@router.get("/{organism_id}")
def obter_pagina_formiga(
    organism_id: int,
    db: Session = Depends(get_db)
):
    resultado = buscar_pagina_formiga(db, organism_id)

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Formiga não encontrada."
        )

    return resultado




@router.get("/{organism_id}/fungi")
def obter_fungos_da_formiga(
    organism_id: int,
    db: Session = Depends(get_db)
):
    resultado = buscar_fungos_da_formiga(db, organism_id)

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Formiga não encontrada."
        )

    return resultado
