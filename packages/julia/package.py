from lib.build_systems.binary import BinaryPackage


class Julia(BinaryPackage):
    """The Julia Language: A fresh approach to technical computing"""

    homepage = "https://julialang.org"

    def url_for_version(self, version):
        major_minor = ".".join(version.split(".")[:2])
        return f"https://julialang-s3.julialang.org/bin/linux/x64/{major_minor}/julia-{version}-linux-x86_64.tar.gz"

    versions = [
        "1.11.7",
    ]
