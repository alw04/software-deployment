from lib.dependency import Dependency
from lib.package import Package


class Repeatmodeler(Package):
    """RepeatModeler is a de-novo repeat family identification and modeling
    package."""

    homepage = "https://www.repeatmasker.org/RepeatModeler/"
    url = "https://github.com/Dfam-consortium/RepeatModeler/archive/refs/tags/{version}.tar.gz"

    versions = [
        "2.0.4",
    ]

    depends_on = [
        Dependency("perl", type=("build", "run")),
        Dependency("perl-json", type=("build", "run")),
        Dependency("perl-libwww-perl", type=("build", "run")),  #####
        Dependency("perl-http-message", type=("build", "run")),
        Dependency("perl-clone", type=("build", "run")),
        Dependency("perl-uri", type=("build", "run")),
        Dependency("perl-http-date", type=("build", "run")),
        Dependency("perl-try-tiny", type=("build", "run")),  #####
        Dependency("perl-file-which", type=("build", "run")),
        Dependency("perl-devel-size", type=("build", "run")),
        Dependency("repeatmasker", type="run"),
        Dependency("recon", type="run"),
        Dependency("repeatscout", type="run"),
        Dependency("trf", type="run"),
        Dependency("cdhit", type="run"),
        Dependency("kentutils", type="run"),
        Dependency("rmblast", type="run"),
    ]

    def configure(self):
        self.run_cmd(
            [
                str(self.build_dir / "configure"),
                "-repeatmasker_dir",
                f"{self.dep('repeatmasker').prefix}/bin",
                "-recon_dir",
                f"{self.dep('recon').prefix}/bin",
                "-rscout_dir",
                f"{self.dep('repeatscout').prefix}/bin",
                "-trf_dir",
                f"{self.dep('trf').prefix}/bin",
                "-cdhit_dir",
                f"{self.dep('cdhit').prefix}/bin",
                "-ucsctools_dir",
                f"{self.dep('kentutils').prefix}/bin",
                "-rmblast_dir",
                f"{self.dep('rmblast').prefix}/bin",
            ],
            cwd=self.build_dir,
            input="\nn\n",
        )

    def install(self):
        self.install_directory(self.build_dir, self.prefix / "bin")
