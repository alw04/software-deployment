from lib.build_systems.autotools import AutotoolsPackage


class Tar(AutotoolsPackage):
    """GNU Tar provides the ability to create tar archives, as well as various
    other kinds of manipulation."""

    homepage = "https://www.gnu.org/software/tar/"
    url = "https://ftp.gnu.org/gnu/tar/tar-{version}.tar.gz"

    versions = [
        "1.35",
    ]
