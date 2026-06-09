from lib.build_systems.autotools import AutotoolsPackage


class Expat(AutotoolsPackage):
    """Expat is an XML parser library written in C."""

    homepage = "https://libexpat.github.io/"

    def url_for_version(self, version):
        version_underscored = version.replace(".", "_")
        return f"https://github.com/libexpat/libexpat/releases/download/R_{version_underscored}/expat-{version}.tar.xz"

    versions = [
        "2.7.1",
    ]
