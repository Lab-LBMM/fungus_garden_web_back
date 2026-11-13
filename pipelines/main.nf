
nextflow.enable.dsl=2
def repoRoot = projectDir.resolve('..').normalize()
params.asv_fasta = null

// Processo responsável pela importação de ASVs
process IMPORT_ASV {

    tag "Importação de ASVs"

    // A importação altera o banco de dados diretamente.
    // Evita que o Nextflow pule a execução por causa do cache.
    cache false

    input:
    path fasta

    script:
    """
    "${repoRoot}/venv/bin/python" \
        "${repoRoot}/scripts/import_asv_fasta.py" \
        "${fasta}"
    """
}

// Workflow principal
workflow {

    // Verifica se o usuário informou o arquivo
    if (!params.asv_fasta) {
        error "Informe o caminho do FASTA usando --asv_fasta"
    }

    // Localiza e verifica o arquivo informado
    asv_file = Channel.fromPath(
        params.asv_fasta,
        checkIfExists: true
    )

    // Executa a importação
    IMPORT_ASV(asv_file)
}
 