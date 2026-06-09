from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Gimp(AutotoolsPackage):
    """GIMP is a cross-platform image editor available for GNU/Linux,
    macOS, Windows and more operating systems. It is free software,
    you can change its source code and distribute your changes.

    Whether you are a graphic designer, photographer, illustrator, or
    scientist, GIMP provides you with sophisticated tools to get your job
    done. You can further enhance your productivity with GIMP thanks to
    many customization options and 3rd party plugins."""

    homepage = "https://www.gimp.org"

    def url_for_version(self, version):
        major_minor = ".".join(version.split(".")[:2])
        return f"https://download.gimp.org/gimp/v{major_minor}/gimp-{version}.tar.bz2"

    versions = [
        "2.10.38",
    ]

    depends_on = [
        Dependency("pango"),
    ]
