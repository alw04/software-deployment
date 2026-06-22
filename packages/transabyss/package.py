from lib.build_systems.binary import BinaryPackage


class Transabyss(BinaryPackage):
    """De novo assembly of RNAseq data using ABySS"""

    homepage = "https://www.bcgsc.ca/platform/bioinfo/software/trans-abyss"
    url = "https://www.bcgsc.ca/platform/bioinfo/software/trans-abyss/releases/{version}/transabyss-{version}.zip"

    versions = [
        "1.5.5",
    ]
