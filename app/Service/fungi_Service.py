
from sqlalchemy.orm import Session, joinedload

from app.Models.organism import Organism


def buscar_fungo_por_id(db: Session, organism_id: int):
    return (
        db.query(Organism)
        .options(
            joinedload(Organism.fungis),
            joinedload(Organism.organism_detail)
        )
        .filter(
            Organism.id == organism_id,
            Organism.type == "Fungo"
        )
        .first()
    )


# GET 1 — Cabeçalho do fungo
def buscar_pagina_fungo(db: Session, organism_id: int):
    fungo = buscar_fungo_por_id(db, organism_id)

    if fungo is None:
        return None

    return {
        "id": fungo.id,
        "nome_cientifico": fungo.name,
        "nome_comum": fungo.common_name,
        "tags": fungo.tags or [],
        "imagem": fungo.image_url,
        "morfologia": fungo.morphology
    }


# GET 2 — Descrição do fungo
def buscar_descricao_fungo(db: Session, organism_id: int):
    fungo = buscar_fungo_por_id(db, organism_id)

    if fungo is None:
        return None

    detalhe = fungo.organism_detail

    return {
        "id": fungo.id,
        "nome_cientifico": fungo.name,
        "descricao": detalhe.description if detalhe else None,
        "habitat": detalhe.habitat if detalhe else None
    }


# GET 3 — Caracterização fúngica especializada
def buscar_caracteristicas_fungo(db: Session, organism_id: int):
    fungo = buscar_fungo_por_id(db, organism_id)

    if fungo is None:
        return None

    atributos = fungo.fungis

    return {
        "id": fungo.id,
        "nome_cientifico": fungo.name,
        "tipo_esporos": atributos.spores if atributos else None,
        "tipo_micelio": atributos.mycelium_type if atributos else None,
        "producao_gongilidios": (
            atributos.gongylidia_production if atributos else None
        ),
        "substrato_crescimento": (
            atributos.growth_substrate if atributos else None
        ),
        "funcao_ecologica_simbiotica": (
            atributos.symbiotic_role if atributos else None
        ),
        "atividade_enzimatica_secretada": (
            atributos.enzymatic_activity if atributos else None
        )
    }
