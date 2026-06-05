from lib.build_systems.meson import MesonPackage


class Libfuse(MesonPackage):
    """The reference implementation of the Linux FUSE (Filesystem in
    Userspace) interface"""

    homepage = "https://github.com/libfuse/libfuse"
    url = "https://github.com/libfuse/libfuse/releases/download/fuse-{version}/fuse-{version}.tar.gz"

    versions = [
        "3.16.2",
    ]

    def meson_args(self):
        return [
            "-Dutils=false",
        ]
