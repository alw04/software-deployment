from lib.build_systems.autotools import AutotoolsPackage


class Mpich(AutotoolsPackage):
    """MPICH is a high performance and widely portable implementation of
    the Message Passing Interface (MPI) standard."""

    homepage = "https://www.mpich.org"
    url = "https://www.mpich.org/static/downloads/{version}/mpich-{version}.tar.gz"

    versions = [
        "4.3.1",
    ]
