from lib.build_systems.autotools import AutotoolsPackage


class Trf(AutotoolsPackage):
    """Tandem Repeats Finder is a program to locate and display tandem repeats
    in DNA sequences."""

    homepage = "https://tandem.bu.edu/trf/trf.html"
    url = "https://github.com/Benson-Genomics-Lab/TRF/archive/refs/tags/v{version}.tar.gz"

    versions = [
        "4.09.1",
    ]
