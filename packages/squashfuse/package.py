from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Squashfuse(AutotoolsPackage):
    """squashfuse - Mount SquashFS archives using FUSE"""

    homepage = "https://github.com/vasi/squashfuse"
    url = "https://github.com/vasi/squashfuse/releases/download/{version}/squashfuse-{version}.tar.gz"

    versions = [
        "0.6.1",
    ]

    depends_on = [
        Dependency("libfuse"),
    ]
