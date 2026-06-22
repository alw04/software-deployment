from lib.build_systems.autotools import AutotoolsPackage


class Gmake(AutotoolsPackage):
    """GNU Make is a tool which controls the generation of executables and
    other non-source files of a program from the program's source files."""

    homepage = "https://www.gnu.org/software/make/"
    url = "https://ftp.gnu.org/gnu/make/make-{version}.tar.gz"

    versions = [
        "4.4.1",
    ]
