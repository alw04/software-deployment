from lib.build_systems.autotools import AutotoolsPackage


class Openmpi(AutotoolsPackage):
    """An open source Message Passing Interface implementation.

    The Open MPI Project is an open source Message Passing Interface
    implementation that is developed and maintained by a consortium
    of academic, research, and industry partners. Open MPI is
    therefore able to combine the expertise, technologies, and
    resources from all across the High Performance Computing
    community in order to build the best MPI library available.
    Open MPI offers advantages for system and software vendors,
    application developers and computer science researchers.
    """

    homepage = "https://www.open-mpi.org"

    def url_for_version(self, version):
        major_minor = ".".join(version.split(".")[:2])
        return f"https://download.open-mpi.org/release/open-mpi/v{major_minor}/openmpi-{version}.tar.bz2"

    versions = [
        "5.0.8",
    ]

    def configure_args(self):
        return [
            "--with-slurm",
            "--disable-dlopen",
        ]
