from lib.build_systems.autotools import AutotoolsPackage


class Bash(AutotoolsPackage):
    """The GNU Project's Bourne Again SHell."""

    homepage = "https://www.gnu.org/software/bash/"
    url = "https://ftp.gnu.org/gnu/bash/bash-{version}.tar.gz"

    versions = [
        "5.3",
    ]
