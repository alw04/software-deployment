from lib.build_systems.autotools import AutotoolsPackage


class Datamash(AutotoolsPackage):
    """GNU datamash is a command-line program which performs basic numeric,
    textual and statistical operations on input textual data files.
    """

    homepage = "https://www.gnu.org/software/datamash/"
    url = "https://ftp.gnu.org/gnu/datamash/datamash-{version}.tar.gz"

    versions = [
        "1.8",
    ]
