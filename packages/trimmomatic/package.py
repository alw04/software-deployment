from lib.build_systems.binary import BinaryPackage


class Trimmomatic(BinaryPackage):
    """A flexible read trimming tool for Illumina NGS data."""

    homepage = "http://www.usadellab.org/cms/?page=trimmomatic"
    url = "http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-{version}.zip"

    versions = [
        "0.39",
    ]
