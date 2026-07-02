from lib.build_systems.python import PythonSourcePackage


class Superfocus(PythonSourcePackage):
    """A tool for agile functional analysis of shotgun metagenomic data"""

    homepage = "https://github.com/metageni/SUPER-FOCUS"
    url = "https://github.com/metageni/SUPER-FOCUS/archive/refs/tags/{version}.tar.gz"

    versions = [
        "1.5",
    ]

    def install(self):
        super().install()

        # downgrade setuptools for pkg_resources requirement
        self.run_cmd([str(self.venv_python), "-m", "pip", "install", "--upgrade", "setuptools<81"])
