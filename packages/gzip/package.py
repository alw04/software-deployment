from lib.build_systems.autotools import AutotoolsPackage


class Gzip(AutotoolsPackage):
    """GNU Gzip is a popular data compression program originally written by
    Jean-loup Gailly for the GNU project."""

    homepage = "https://www.gnu.org/software/gzip/"
    url = "https://ftp.gnu.org/gnu/gzip/gzip-{version}.tar.gz"

    versions = [
        "1.13",
    ]
