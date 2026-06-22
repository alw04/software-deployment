from lib.build_systems.binary import BinaryPackage


class WgsAssembler(BinaryPackage):
    """Celera Assembler (CA) is a whole-genome shotgun (WGS) assembler
    for the reconstruction of genomic DNA sequence from WGS sequencing data.
    """

    homepage = "https://sourceforge.net/projects/wgs-assembler/"

    urls_by_version = {
        "8.3rc2": "https://sourceforge.net/projects/wgs-assembler/files/wgs-assembler/wgs-8.3/wgs-8.3rc2-Linux_amd64.tar.bz2",
        "8.3rc1": "https://sourceforge.net/projects/wgs-assembler/files/wgs-assembler/wgs-8.3/wgs-8.3rc1-Linux_amd64.tar.bz2",
    }

    versions = [
        "8.3rc2",
        "8.3rc1",
    ]

    source_subdir = "Linux-amd64"
