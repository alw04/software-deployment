from lib.build_systems.makefile import MakefilePackage


class SoapdenovoTrans(MakefilePackage):
    """SOAPdenovo-Trans is a de novo transcriptome assembler basing on the
    SOAPdenovo framework, adapt to alternative splicing and different
    expression level among transcripts."""

    homepage = "https://github.com/aquaskyline/SOAPdenovo-Trans"
    url = "https://github.com/aquaskyline/SOAPdenovo-Trans/archive/refs/tags/{version}.tar.gz"

    versions = [
        "1.0.5",
    ]

    source_subdir = "src"

    def build(self):
        targets = [
            ["make"],
            ["make", "127mer=1"],
            ["make", "63mer=1"],
        ]

        for cmd in targets:
            self.run_cmd(cmd, cwd=self.build_dir)

    def install(self):
        for binary in sorted(self.build_path.glob("SOAPdenovo-Trans-*mer")):
            self.install_binary(binary)
