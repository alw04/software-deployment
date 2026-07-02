from lib.build_systems.makefile import MakefilePackage


class Soapdenovo2(MakefilePackage):
    """SOAPdenovo is a novel short-read assembly method that can build a de
    novo draft assembly for the human-sized genomes. The program is
    specially designed to assemble Illumina GA short reads. It creates
    new opportunities for building reference sequences and carrying out
    accurate analyses of unexplored genomes in a cost effective way."""

    homepage = "https://github.com/aquaskyline/SOAPdenovo2"
    url = "https://github.com/aquaskyline/SOAPdenovo2/archive/r{version}.tar.gz"

    versions = [
        "242",
    ]

    def install(self):
        for binary in sorted(self.build_path.glob("SOAPdenovo-*mer")):
            self.install_binary(binary)
