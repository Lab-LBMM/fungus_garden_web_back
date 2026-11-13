from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.Service.organism_Service import (
    contar_organismos,
    contar_por_tipo, 
    listar_morfologias
)

router = APIRouter(prefix="/organisms", tags=["Organisms"])


@router.get("/count")
def obter_total_organismos(db: Session = Depends(get_db)):
    return {"quantidade": contar_organismos(db)}


@router.get("/count/fungi")
def obter_total_fungos(db: Session = Depends(get_db)):
    return {"quantidade": contar_por_tipo(db, "Fungo")}


@router.get("/count/bacteria")
def obter_total_bacterias(db: Session = Depends(get_db)):
    return {"quantidade": contar_por_tipo(db, "Bacteria")}


@router.get("/count/ants")
def obter_total_formigas(db: Session = Depends(get_db)):
    return {"quantidade": contar_por_tipo(db, "Formiga")}

@router.get("/morphologies")
def obter_morfologias(db: Session = Depends(get_db)):
    morfologias = listar_morfologias(db)

    return [morfologia[0] for morfologia in morfologias]