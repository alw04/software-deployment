from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Abyss(AutotoolsPackage):
    """ABySS is a de novo, parallel, paired-end sequence assembler
    that is designed for short reads. The single-processor version
    is useful for assembling genomes up to 100 Mbases in size."""

    homepage = "https://www.bcgsc.ca/platform/bioinfo/software/abyss"
    url = "https://github.com/bcgsc/abyss/releases/download/{version}/abyss-{version}.tar.gz"

    versions = [
        "2.3.10",
    ]

    depends_on = [
        Dependency("boost"),
        Dependency("btllib"),
        Dependency("sparsehash"),
    ]

    def configure(self):
        self.append_env("CXXFLAGS", "-std=c++17")
        super().configure()
