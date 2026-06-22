from lib.build_systems.binary import BinaryPackage
from lib.dependency import Dependency


class Trinotate(BinaryPackage):
    """Trinotate is a comprehensive annotation suite designed for
    automatic functional annotation of transcriptomes, particularly
    de novo assembled transcriptomes, from model or non-model organisms"""

    homepage = "https://trinotate.github.io/"
    url = "https://github.com/Trinotate/Trinotate/archive/Trinotate-v{version}.tar.gz"

    versions = [
        "3.2.2",
    ]

    depends_on = [
        Dependency("perl", type="run"),
        Dependency("sqlite", type="run"),
    ]
