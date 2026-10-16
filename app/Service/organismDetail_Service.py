from sqlalchemy.orm import Session

from app.Models.organismDetail import OrganismDetail


def buscar_descricao(db: Session, organism_id: int):
    detalhe = (
        db.query(OrganismDetail)
        .filter(OrganismDetail.organism_id == organism_id)
        .first()
    )

    if detalhe is None:
        return None

    return detalhe.description