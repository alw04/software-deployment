from lib.build_systems.autotools import AutotoolsPackage


class Vsearch(AutotoolsPackage):
    """VSEARCH is a versatile open-source tool for metagenomics."""

    homepage = "https://github.com/torognes/vsearch"
    url = "https://github.com/torognes/vsearch/archive/v{version}.tar.gz"

    versions = [
        "2.22.1",
    ]
