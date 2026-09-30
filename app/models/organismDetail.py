from sqlalchemy import Column, Integer, Numeric, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class OrganismDetail(Base):
    __tablename__ = "organism_details"

    id = Column(Integer,ForeignKey("organism.id", ondelete="CASCADE"),primary_key=True)
    genome_size = Column(Numeric(10, 2), nullable=True )
    gc_content = Column(Numeric(5, 2), nullable=True)
    gene_count = Column(Integer,nullable=True)
    description = Column(Text, nullable=True)
    habitat = Column(Text,nullable=True)
    genbank_accession = Column(Text,nullable=True)
    hero_image_url = Column( Text, nullable=True)
    organism = relationship( "Organism", back_populates="organism_detail")