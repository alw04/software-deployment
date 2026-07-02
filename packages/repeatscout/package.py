from lib.build_systems.makefile import MakefilePackage


class Repeatscout(MakefilePackage):
    """RepeatScout - De Novo Repeat Finder, Price A.L., Jones N.C. and Pevzner
    P.A."""

    homepage = "https://www.repeatmasker.org/RepeatModeler/"
    url = "https://github.com/Dfam-consortium/RepeatScout/archive/refs/tags/v{version}.tar.gz"

    versions = [
        "1.0.7",
    ]

    def install_args(self):
        return [
            f"INSTDIR={self.prefix}/bin",
        ]
