from lib.build_systems.makefile import MakefilePackage


class Unicycler(MakefilePackage):
    """Unicycler is an assembly pipeline for bacterial genomes."""

    homepage = "https://github.com/rrwick/Unicycler"
    url = "https://github.com/rrwick/Unicycler/archive/refs/tags/v{version}.tar.gz"

    versions = [
        "0.5.1",
    ]

    def install(self):
        self.install_binary(self.build_dir / "unicycler-runner.py")
