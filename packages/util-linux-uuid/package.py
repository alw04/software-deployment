from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class UtilLinuxUuid(AutotoolsPackage):
    """Util-linux is a suite of essential utilities for any Linux system."""

    homepage = "https://github.com/util-linux/util-linux"
    url = "https://www.kernel.org/pub/linux/utils/util-linux/v{version}/util-linux-{version}.tar.gz"

    versions = [
        "2.41",
    ]

    depends_on = [
        Dependency("sqlite"),
    ]

    def configure_args(self):
        return [
            "--disable-all-programs",
            "--enable-libuuid",
        ]
