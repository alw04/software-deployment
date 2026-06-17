from lib.build_systems.container import ContainerPackage


class Gimp(ContainerPackage):
    """GIMP is a cross-platform image editor available for GNU/Linux,
    macOS, Windows and more operating systems. It is free software,
    you can change its source code and distribute your changes.

    Whether you are a graphic designer, photographer, illustrator, or
    scientist, GIMP provides you with sophisticated tools to get your job
    done. You can further enhance your productivity with GIMP thanks to
    many customization options and 3rd party plugins."""

    homepage = "https://www.gimp.org"
    image = "docker://minidocks/gimp:{version}"

    versions = [
        "2.10",
    ]

    shell_functions = {
        "gimp": "gimp",
    }
