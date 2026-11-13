
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.Service.bacterium_Service import (
    buscar_caracterizacao_bacteriana,
    buscar_bacteria_por_id
)

router = APIRouter(
     prefix="/bacterium",
    tags=["Bacterium"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/organisms/{organism_id}/bacterial-characteristics")
def get_caracterizacao_bacteriana(
    organism_id: int,
    db: Session = Depends(get_db)
):
    caracterizacao = buscar_caracterizacao_bacteriana(
        db,
        organism_id
    )

    if caracterizacao is None:
        raise HTTPException(
            status_code=404,
            detail="Caracterização bacteriana não encontrada"
        )

    return caracterizacao



@router.get("/{organism_id}")
def obter_bacteria(
    organism_id: int,
    db: Session = Depends(get_db)
):
    bacteria = buscar_bacteria_por_id(db, organism_id)

    if bacteria is None:
        raise HTTPException(
            status_code=404,
            detail="Bactéria não encontrada."
        )

    return bacteria