from lib.build_systems.meson import MesonPackage
from lib.dependency import Dependency


class Btllib(MesonPackage):
    """Bioinformatics Technology Lab common code library in C++
    with Python wrappers.
    """

    homepage = "https://github.com/bcgsc/btllib"
    url = "https://github.com/bcgsc/btllib/releases/download/v{version}/btllib-{version}.tar.gz"

    versions = [
        "1.7.5",
    ]

    depends_on = [
        Dependency("samtools", type=("build", "run")),
        Dependency("python@3.11.0", type=("build", "run")),
    ]

    phases = (
        "download",
        "extract",
        "install",
    )

    def install(self):
        self.run_cmd([str(self.build_dir / "compile"), f"--prefix={self.prefix}"], cwd=self.build_dir)
