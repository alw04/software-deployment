from lib.build_systems.cmake import CMakePackage
from lib.dependency import Dependency


class Revbayes(CMakePackage):
    """Bayesian phylogenetic inference using probabilistic graphical models
    and an interpreted language."""

    homepage = "https://revbayes.github.io"
    url = "https://github.com/revbayes/revbayes/archive/refs/tags/v{version}.tar.gz"

    versions = [
        "1.2.2",
    ]

    depends_on = [
        Dependency("boost"),
        Dependency("openmpi"),
    ]

    phases = (
        "download",
        "extract",
        "build",
        "install",
    )

    @property
    def cmake_dir(self):
        return self.build_dir / "projects" / "cmake"

    def build(self):
        self.run_cmd(
            [
                str(self.cmake_dir / "build.sh"),
                "-mpi",
                "true",
                "-boost_root",
                f"{self.dep('boost').prefix}",
            ],
            cwd=self.cmake_dir,
        )

    def install(self):
        self.install_binary(self.cmake_dir / "rb-mpi")
