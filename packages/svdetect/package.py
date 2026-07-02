from lib.build_systems.binary import BinaryPackage


class Svdetect(BinaryPackage):
    """A tool to identify genomic structural variations from paired-end and mate-pair sequencing data"""

    homepage = "https://svdetect.sourceforge.net/Site/Home.html"

    def url_for_version(self, version):
        folder = f"{float(version.rstrip('abcdefghijklmnopqrstuvwxyz')):.2f}"
        return f"https://sourceforge.net/projects/svdetect/files/SVDetect/{folder}/SVDetect_r{version}.tar.gz"

    versions = [
        "0.8b",
    ]
