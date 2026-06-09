from lib.build_systems.meson import MesonPackage


class Pango(MesonPackage):
    """Pango is a library for laying out and rendering of text, with
    an emphasis on internationalization. It can be used anywhere
    that text layout is needed, though most of the work on Pango so
    far has been done in the context of the GTK+ widget toolkit."""

    homepage = "https://www.pango.org"

    def url_for_version(self, version):
        major_minor = ".".join(version.split(".")[:2])
        return f"http://ftp.gnome.org/pub/GNOME/sources/pango/{major_minor}/pango-{version}.tar.xz"

    versions = [
        "1.54.0",
    ]
