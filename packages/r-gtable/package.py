from lib.build_systems.r import RPackage
from lib.dependency import Dependency


class RGtable(RPackage):
    """Arrange 'Grobs' in Tables.

    Tools to make it easier to work with "tables" of 'grobs'. The 'gtable'
    package defines a 'gtable' grob class that specifies a grid along with a
    list of grobs and their placement in the grid. Further the package makes it
    easy to manipulate and combine 'gtable' objects so that complex
    compositions can be build up sequentially."""

    homepage = "https://gtable.r-lib.org/"
    cran = "gtable"

    versions = [
        "0.3.6",
    ]

    depends_on = [
        Dependency("r-cli", type=("build", "run")),
        Dependency("r-glue", type=("build", "run")),
        Dependency("r-lifecycle", type=("build", "run")),
        Dependency("r-rlang", type=("build", "run")),
    ]
