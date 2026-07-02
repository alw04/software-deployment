from lib.build_systems.cmake import CMakePackage
from lib.dependency import Dependency

class Salmon(CMakePackage):
    """Salmon is a tool for quantifying the expression of transcripts using
    RNA-seq data."""

    homepage = "https://combine-lab.github.io/salmon/"
    url = "https://github.com/COMBINE-lab/salmon/archive/v{version}.tar.gz"

    versions = [
        "1.10.3",
    ]

    depends_on = [
        Dependency("boost"),
    ]
