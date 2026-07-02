from lib.build_systems.autotools import AutotoolsPackage


class TrnascanSe(AutotoolsPackage):
    """Seaching for tRNA genes in genomic sequence"""

    homepage = "http://lowelab.ucsc.edu/tRNAscan-SE/"
    url = "http://trna.ucsc.edu/software/trnascan-se-{version}.tar.gz"

    versions = [
        "2.0.12",
    ]

    download_headers = {
        "User-Agent": "Mozilla/5.0",
    }
