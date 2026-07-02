from lib.build_systems.binary import BinaryPackage


class Sratoolkit(BinaryPackage):
    """The NCBI SRA Toolkit enables reading ("dumping") of sequencing files
    from the SRA database and writing ("loading") files into the .sra
    format."""

    homepage = "https://trace.ncbi.nlm.nih.gov/Traces/sra"
    url = "https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/{version}/sratoolkit.{version}-centos_linux64.tar.gz"

    versions = [
        "3.0.0",
    ]
