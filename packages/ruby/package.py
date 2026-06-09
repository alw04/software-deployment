from lib.build_systems.autotools import AutotoolsPackage


class Ruby(AutotoolsPackage):
    """A dynamic, open source programming language with a focus on
    simplicity and productivity.
    """

    homepage = "https://www.ruby-lang.org/"

    def url_for_version(self, version):
        major_minor = ".".join(version.split(".")[:2])
        return f"https://cache.ruby-lang.org/pub/ruby/{major_minor}/ruby-{version}.tar.gz"

    versions = [
        "3.3.5",
    ]
