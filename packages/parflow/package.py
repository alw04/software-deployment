from lib.build_systems.cmake import CMakePackage
from lib.dependency import Dependency


class Parflow(CMakePackage):
    """ParFlow is an open-source parallel watershed simulator which
    includes overland flow, complex topology, heterogeneity and coupled
    land-surface processes."""

    homepage = "https://www.parflow.org/"
    url = "https://github.com/parflow/parflow/archive/v{version}.tar.gz"

    versions = [
        "3.9.0",
    ]

    depends_on = [
        Dependency("tcl"),
    ]
