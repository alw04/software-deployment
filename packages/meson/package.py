from lib.build_systems.python import PythonPackage


class Meson(PythonPackage):
    """Meson is a portable open source build system meant to be both
    extremely fast, and as user friendly as possible."""

    homepage = "https://mesonbuild.com/"
    url = "https://github.com/mesonbuild/meson/archive/{version}.tar.gz"

    versions = [
        "1.8.2",
    ]
