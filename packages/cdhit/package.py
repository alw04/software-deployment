from lib.build_systems.makefile import MakefilePackage


class Cdhit(MakefilePackage):
    """CD-HIT is a very widely used program for clustering and comparing
    protein or nucleotide sequences."""

    homepage = "http://cd-hit.org/"
    url = "https://github.com/weizhongli/cdhit/archive/V{version}.tar.gz"

    versions = [
        "4.8.1",
    ]

    def install(self):
        bin_dir = self.prefix / "bin"
        bin_dir.mkdir(parents=True, exist_ok=True)
        self.run_cmd(["make", "install", f"PREFIX={bin_dir}"], cwd=self.build_dir)
