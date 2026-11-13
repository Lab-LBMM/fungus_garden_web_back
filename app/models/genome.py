from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Genome(Base):
    __tablename__ = "genomes"

    id            = Column(Integer, primary_key=True, autoincrement=True, index=True)
    accession     = Column(String(50),  nullable=False, unique=True)
    assembly_name = Column(String(100), nullable=False)
    data_source   = Column(String(50),  nullable=True)
    import_date   = Column(DateTime,    server_default=func.now())
    organism_id   = Column(Integer, ForeignKey("organisms.id", ondelete="CASCADE"), nullable=False, index=True)

    # ── Relacionamentos ──────────────────────────────────────────────────────
    organism         = relationship("Organism",        back_populates="genomes")
    genome_sequences = relationship("GenomeSequence",  back_populates="genome")
