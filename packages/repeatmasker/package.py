from lib.dependency import Dependency
from lib.package import Package


class Repeatmasker(Package):
    """RepeatMasker is a program that screens DNA sequences for interspersed
    repeats and low complexity DNA sequences."""

    homepage = "https://www.repeatmasker.org"
    url = "https://www.repeatmasker.org/RepeatMasker/RepeatMasker-{version}.tar.gz"

    versions = [
        "4.2.4",
    ]

    depends_on = [
        Dependency("trf", type="run"),
        Dependency("rmblast", type="run"),
        Dependency("h5py", type="run"),
        Dependency("famdb", type="run"),
    ]

    def configure(self):
        self.run_cmd(
            [
                str(self.build_dir / "configure"),
                "-trf_prgm",
                f"{self.dep('trf').prefix}/bin/trf",
                "-rmblast_dir",
                f"{self.dep('rmblast').prefix}/bin",
                "-famdb_dir",
                f"{self.dep('famdb').prefix}/bin",
            ],
            cwd=self.build_dir,
        )

    def install(self):
        self.install_directory(self.build_dir, self.prefix / "bin")
