from lib.build_systems.makefile import MakefilePackage


class Yaggo(MakefilePackage):
    """Yaggo is a tool to generate command line parsers for C++.
    Yaggo stands for "Yet Another GenGetOpt" and is inspired by GNU Gengetopt.
    """

    homepage = "https://github.com/gmarcais/yaggo"
    url = "https://github.com/gmarcais/yaggo/archive/refs/tags/v{version}.tar.gz"

    versions = [
        "1.5.11",
    ]

    def install_args(self):
        return [
            f"prefix={self.prefix}",
        ]
