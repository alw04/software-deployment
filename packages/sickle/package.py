from lib.build_systems.makefile import MakefilePackage


class Sickle(MakefilePackage):
    """Sickle is a tool that uses sliding windows along with quality and
    length thresholds to determine when quality is sufficiently low to trim
    the 3'-end of reads and also determines when the quality is
    sufficiently high enough to trim the 5'-end of reads."""

    homepage = "https://github.com/najoshi/sickle"
    url = "https://github.com/najoshi/sickle/archive/v{version}.tar.gz"

    versions = [
        "1.33",
    ]

    def install(self):
        self.install_binary(self.build_dir / "sickle")
