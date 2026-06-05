from lib.dependency import Dependency
from lib.package import Package


class PythonPackage(Package):
    abstract = True

    phases = (
        "download",
        "extract",
        "install",
    )

    depends_on = [
        Dependency("python", type=("build", "run")),
    ]

    def install(self):
        self.run_cmd(
            ["python", "-m", "pip", "install", ".", "--prefix", str(self.prefix), "--no-deps"], cwd=self.build_dir
        )
