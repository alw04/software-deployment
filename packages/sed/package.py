from lib.build_systems.autotools import AutotoolsPackage


class Sed(AutotoolsPackage):
    """GNU implementation of the famous stream editor."""

    homepage = "https://www.gnu.org/software/sed/"
    url = "https://ftp.gnu.org/gnu/sed/sed-{version}.tar.xz"

    versions = [
        "4.9",
    ]
