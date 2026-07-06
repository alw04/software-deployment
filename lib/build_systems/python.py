import sysconfig
from pathlib import Path

from lib.dependency import Dependency
from lib.package import Package


class PythonPackage(Package):
    abstract = True

    phases = ("install",)

    depends_on = [
        Dependency("python", type="build"),  # runtime uses the package's own venv
    ]

    @property
    def python_lib(self):
        site = sysconfig.get_path("purelib", vars={"base": str(self.prefix)})
        return {
            "PYTHONPATH": [Path(site)],
        }

    def additional_build_env(self):
        return self.python_lib

    def modulefile_prepend_path(self):
        return self.python_lib

    @property
    def venv_python(self) -> Path:
        return self.prefix / "bin" / "python"

    def create_venv(self):
        self.run_cmd(["python3", "-m", "venv", "--clear", str(self.prefix)])
        self.run_cmd([str(self.venv_python), "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])

    def install(self):
        self.create_venv()

        self.run_cmd(
            [
                str(self.venv_python),
                "-m",
                "pip",
                "install",
                f"{self.name}=={self.version}",
                # "--no-deps",
            ]
        )


class PythonSourcePackage(PythonPackage):
    abstract = True

    phases = (
        "download",
        "extract",
        "install",
    )

    def install(self):
        self.create_venv()
        self.run_cmd([str(self.venv_python), "-m", "pip", "install", "."], cwd=self.build_dir)
