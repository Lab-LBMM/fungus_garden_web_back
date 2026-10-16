
from sqlalchemy.orm import Session,joinedload
from app.Models.bacterium import Bacterium
from app.Models.organism import Organism

def buscar_caracterizacao_bacteriana(
    db: Session,
    organism_id: int
):
    bacteria = (
        db.query(Bacterium)
        .filter(Bacterium.organism_id == organism_id)
        .first()
    )

    if bacteria is None:
        return None

    return {
        "organism_id": bacteria.organism_id,
        "gram_stain": bacteria.gram_stain,
        "motility": bacteria.motility
    }




def buscar_bacteria_por_id(db: Session, organism_id: int):
    bacteria = (
        db.query(Organism)
        .options(
            joinedload(Organism.bacterium),
            joinedload(Organism.organism_detail)
        )
        .filter(
            Organism.id == organism_id,
            Organism.type == "Bacteria"
        )
        .first()
    )

    if bacteria is None:
        return None

    bacterium = bacteria.bacterium
    detail = bacteria.organism_detail

    return {
        "id": bacteria.id,
        "nome_cientifico": bacteria.name,
        "nome_comum": bacteria.common_name,
        "tipo": bacteria.type,
        "morfologia": bacteria.morphology,
        "tags": bacteria.tags or [],
        "imagem": (
            detail.hero_image_url
            if detail and detail.hero_image_url
            else bacteria.image_url
        ),
        "cor": bacteria.color,

        "caracteristicas": {
            "gram": bacterium.gram_stain if bacterium else None,
            "motilidade": bacterium.motility if bacterium else None,
            "esporos": bacterium.spores if bacterium else None,
            "temperatura_otima": (
                bacterium.optimum_temperature if bacterium else None
            ),
            "producao_antibioticos": (
                bacterium.antibiotic_production
                if bacterium else None
            )
        },

        "detalhes": {
            "tamanho_genoma": (
                float(detail.genome_size)
                if detail and detail.genome_size is not None
                else None
            ),
            "conteudo_gc": (
                float(detail.gc_content)
                if detail and detail.gc_content is not None
                else None
            ),
            "quantidade_genes": (
                detail.gene_count if detail else None
            ),
            "descricao": detail.description if detail else None,
            "habitat": detail.habitat if detail else None,
            "genbank_accession": (
                detail.genbank_accession if detail else None
            )
        }
    }

