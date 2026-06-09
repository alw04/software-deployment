from lib.build_systems.autotools import AutotoolsPackage


class Argtable(AutotoolsPackage):
    """Argtable is an ANSI C library for parsing GNU style command line
    options with a minimum of fuss.
    """

    homepage = "https://argtable.sourceforge.net/"
    url = "https://prdownloads.sourceforge.net/argtable/argtable{version}.tar.gz"

    versions = [
        "2-13",
    ]
