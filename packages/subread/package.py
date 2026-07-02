from lib.build_systems.makefile import MakefilePackage


class Subread(MakefilePackage):
    """The Subread software package is a tool kit for processing next-gen
    sequencing data."""

    homepage = "https://subread.sourceforge.net/"
    url = "https://sourceforge.net/projects/subread/files/subread-{version}/subread-{version}-source.tar.gz"

    versions = [
        "2.0.6",
    ]

    source_subdir = "src"

    def build(self):
        self.run_cmd(["make", "-f", "Makefile.Linux"], cwd=self.build_dir)

    def install(self):
        self.install_directory(self.build_path / "bin", self.prefix / "bin")
