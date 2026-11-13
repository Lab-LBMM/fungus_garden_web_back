from sqlalchemy.orm import Session
from app.Models.organism import Organism


def contar_organismos(db: Session):
    return db.query(Organism).count()


def contar_por_tipo(db: Session, tipo: str):
    return db.query(Organism).filter(
        Organism.type == tipo
    ).count() 


def listar_morfologias(db: Session):
    return (
        db.query(Organism.morphology)
        .filter(Organism.morphology.isnot(None))
        .filter(Organism.morphology != "")
        .distinct()
        .order_by(Organism.morphology)
        .all()
    )