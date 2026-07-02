from lib.build_systems.makefile import MakefilePackage


class Star(MakefilePackage):
    """STAR is an ultrafast universal RNA-seq aligner."""

    homepage = "https://github.com/alexdobin/STAR"
    url = "https://github.com/alexdobin/STAR/archive/{version}.tar.gz"

    versions = [
        "2.7.11b",
    ]

    source_subdir = "source"

    def build(self):
        self.run_cmd(["make"], cwd=self.build_dir)
        self.run_cmd(["make", "STARlong"], cwd=self.build_dir)

    def install(self):
        self.install_binary(self.build_dir / "STAR")
        self.install_binary(self.build_dir / "STARlong")
