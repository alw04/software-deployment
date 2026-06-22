from lib.build_systems.autotools import AutotoolsPackage


class Htslib(AutotoolsPackage):
    """C library for high-throughput sequencing data formats."""

    homepage = "https://github.com/samtools/htslib"
    url = "https://github.com/samtools/htslib/releases/download/{version}/htslib-{version}.tar.bz2"

    versions = [
        "1.21",
    ]
