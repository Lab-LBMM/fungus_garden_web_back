
from sqlalchemy.orm import Session, joinedload

from app.Models.organism import Organism
from app.Models.organismAssociation import OrganismAssociation


def buscar_formiga_por_id(db: Session, organism_id: int):
    return (
        db.query(Organism)
        .options(
            joinedload(Organism.ants),
            joinedload(Organism.organism_detail)
        )
        .filter(
            Organism.id == organism_id,
            Organism.type == "Formiga"
        )
        .first()
    )


def buscar_descricao_formiga(db: Session, organism_id: int):
    formiga = buscar_formiga_por_id(db, organism_id)

    if formiga is None:
        return None

    detalhe = formiga.organism_detail

    return {
        "id": formiga.id,
        "nome_cientifico": formiga.name,
        "nome_comum": formiga.common_name,
        "descricao": detalhe.description if detalhe else None,
        "habitat": detalhe.habitat if detalhe else None,
    }


def buscar_organismos_associados(
    db: Session,
    formiga_id: int,
    tipo_organismo: str,
    termos_associacao: list[str]
):
    resultados = (
        db.query(Organism, OrganismAssociation.association_type)
        .join(
            OrganismAssociation,
            OrganismAssociation.target_id == Organism.id
        )
        .filter(
            OrganismAssociation.source_id == formiga_id,
            Organism.type == tipo_organismo
        )
        .all()
    )

    return [
        (organismo, associacao)
        for organismo, associacao in resultados
        if associacao and any(
            termo in associacao.lower()
            for termo in termos_associacao
        )
    ]


def buscar_caracteristicas_formiga(
    db: Session,
    organism_id: int
):
    formiga = buscar_formiga_por_id(db, organism_id)

    if formiga is None:
        return None

    atributos = formiga.ants

    bacterias = buscar_organismos_associados(
        db,
        formiga.id,
        "Bacteria",
        ["simbiose", "simbionte", "symbiosis", "symbiont"]
    )

    fungos = buscar_organismos_associados(
        db,
        formiga.id,
        "Fungo",
        ["cultivo", "cultivada", "jardim", "cultivates", "cultivated_by"]
    )

    return {
        "id": formiga.id,
        "nome_cientifico": formiga.name,
        "tipo_agricultura": (
            atributos.agriculture_type if atributos else None
        ),
        "tamanho_colonia": (
            atributos.colony_size if atributos else None
        ),
        "profundidade_ninho": (
            atributos.nest_depth if atributos else None
        ),
        "sistema_castas": (
            atributos.caste_system if atributos else None
        ),
        "bacterias_simbiontes": [
            {
                "id": organismo.id,
                "nome_cientifico": organismo.name,
                "nome_comum": organismo.common_name,
            }
            for organismo, _ in bacterias
        ],
        "fungos_cultivados": [
            {
                "id": organismo.id,
                "nome_cientifico": organismo.name,
                "nome_comum": organismo.common_name,
            }
            for organismo, _ in fungos
        ]
    }


def buscar_pagina_formiga(db: Session, organism_id: int):
    formiga = buscar_formiga_por_id(db, organism_id)

    if formiga is None:
        return None

    atributos = formiga.ants

    return {
        "id": formiga.id,
        "nome_cientifico": formiga.name,
        "nome_comum": formiga.common_name,
        "tipo": formiga.type,
        "imagem": formiga.image_url,
        "morfologia": formiga.morphology,
        "tags": formiga.tags or [],
        "agricultura": (
            atributos.agriculture_type if atributos else None
        )
    }


def buscar_fungos_da_formiga(db: Session, organism_id: int):
    formiga = (
        db.query(Organism)
        .filter(
            Organism.id == organism_id,
            Organism.type == "Formiga"
        )
        .first()
    )

    if formiga is None:
        return None

    fungos = (
        db.query(Organism.name)
        .join(
            OrganismAssociation,
            Organism.id == OrganismAssociation.target_id
        )
        .filter(
            OrganismAssociation.source_id == organism_id,
            Organism.type == "Fungo"
        )
        .all()
    )

    return [nome[0] for nome in fungos]
