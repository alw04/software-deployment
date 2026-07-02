from lib.build_systems.binary import BinaryPackage
from lib.dependency import Dependency


class Rmblast(BinaryPackage):
    """RMBlast is a RepeatMasker compatible version of the standard NCBI blastn program."""

    homepage = "https://www.repeatmasker.org/rmblast/"
    url = "https://www.repeatmasker.org/rmblast/rmblast-{version}+-x64-linux.tar.gz"

    versions = [
        "2.17.1",
    ]

    depends_on = [
        Dependency("bzip2", type="run"),
    ]
