from lib.build_systems.makefile import MakefilePackage


class Recon(MakefilePackage):
    """RECON: a package for automated de novo identification of repeat families
    from genomic sequences."""

    homepage = "http://eddylab.org/software/recon/"
    url = "http://eddylab.org/software/recon/RECON{version}.tar.gz"

    versions = [
        "1.05",
    ]

    source_subdir = "src"

    def install(self):
        super().install()

        for dir in ["bin", "scripts", "Demos"]:
            self.install_directory(self.build_path / dir, self.prefix / dir)
