from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Sga(AutotoolsPackage):
    """SGA is a de novo genome assembler based on the concept of string graphs.
    The major goal of SGA is to be very memory efficient, which is achieved
    by using a compressed representation of DNA sequence reads."""

    homepage = "https://www.msi.umn.edu/sw/sga"
    url = "https://github.com/jts/sga/archive/v{version}.tar.gz"

    source_subdir = "src"

    versions = [
        "0.10.15",
    ]

    depends_on = [
        Dependency("sparsehash"),
        Dependency("bamtools"),
        Dependency("jemalloc"),
    ]

    def configure_args(self):
        return [
            f"--with-sparsehash={self.dep('sparsehash').prefix}",
            f"--with-bamtools={self.dep('bamtools').prefix}",
            f"--with-jemalloc={self.dep('jemalloc').prefix}",
        ]
