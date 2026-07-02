from lib.build_systems.go import GoPackage


class Seqkit(GoPackage):
    """seqkit: a cross-platform and ultrafast toolkit for FASTA/Q file manipulation"""

    homepage = "https://bioinf.shenwei.me/seqkit/"
    url = "https://github.com/shenwei356/seqkit/archive/refs/tags/v{version}.tar.gz"

    versions = [
        "2.10.0",
    ]

    source_subdir = "seqkit"
