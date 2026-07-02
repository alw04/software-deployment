from lib.build_systems.makefile import MakefilePackage


class Spades(MakefilePackage):
    """SPAdes - St. Petersburg genome assembler - is intended for both
    standard isolates and single-cell MDA bacteria assemblies."""

    homepage = "https://ablab.github.io/spades/"
    url = "https://github.com/ablab/spades/releases/download/v{version}/SPAdes-{version}.tar.gz"

    versions = [
        "4.0.0",
    ]

    def build(self):
        self.run_cmd([str(self.build_dir / "spades_compile.sh")], cwd=self.build_dir)

    def install(self):
        self.install_directory(self.build_dir / "bin", self.prefix / "bin")
        self.install_directory(self.build_dir / "share", self.prefix / "share")
