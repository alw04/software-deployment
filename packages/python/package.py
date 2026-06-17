from lib.build_systems.autotools import AutotoolsPackage


class Python(AutotoolsPackage):
    """The Python programming language."""

    homepage = "https://www.python.org/"
    url = "https://www.python.org/ftp/python/{version}/Python-{version}.tgz"

    versions = [
        "3.14.0",
        "3.11.0",
    ]

    def configure_args(self):
        return [
            "--with-ensurepip=install",
            "--with-pydebug",
        ]

    conflicts = [
        "miniconda3",
    ]
