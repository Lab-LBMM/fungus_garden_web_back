# Importar todas as models para que o SQLAlchemy registre os mapeamentos
# no metadata da Base antes de qualquer create_all() ou migração Alembic.
#
# Ordem de importação respeita as dependências:
#   Taxa → Organism → (Ant, Fungi, Bacterium, OrganismDetail,
#                       OrganismReference, OrganismAssociation)
#             → Genome → GenomeSequence → Gene
#                           → NucleotideSequence
#                           → Protein → ProteinSequence

from .taxa                import Taxa                 # noqa: F401
from .organism            import Organism             # noqa: F401
from .ant                 import Ant                  # noqa: F401
from .fungi               import Fungi                # noqa: F401
from .bacterium           import Bacterium            # noqa: F401
from .organismDetail      import OrganismDetail       # noqa: F401
from .organismReference   import OrganismReference    # noqa: F401
from .organismAssociation import OrganismAssociation  # noqa: F401
from .genome              import Genome               # noqa: F401
from .genome_sequence     import GenomeSequence       # noqa: F401
from .gene                import Gene                 # noqa: F401
from .nucleotide_sequence import NucleotideSequence   # noqa: F401
from .protein             import Protein              # noqa: F401
from .protein_sequence    import ProteinSequence      # noqa: F401
from .sample              import Sample                # noqa: F401
from .sampling            import Sampling              # noqa: F401
from .sample_confection   import SampleConfection      # noqa: F401
from .literature          import Literature            # noqa: F401
from .literature_reference import LiteratureReference  # noqa: F401
from .asv                 import ASV                   # noqa: F401
from .asv_set             import ASVSet                # noqa: F401
from .sequencing_run      import SequencingRun         # noqa: F401
from .sequence            import Sequence              # noqa: F401

__all__ = [
    "Taxa",
    "Organism",
    "Ant",
    "Fungi",
    "Bacterium",
    "OrganismDetail",
    "OrganismReference",
    "OrganismAssociation",
    "Genome",
    "GenomeSequence",
    "Gene",
    "NucleotideSequence",
    "Protein",
    "ProteinSequence",
    "Sample",
    "Sampling",
    "SampleConfection",
    "Literature",
    "LiteratureReference",
    "ASV",
    "ASVSet",
    "SequencingRun",
    "Sequence",
]
