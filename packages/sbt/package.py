from lib.build_systems.binary import BinaryPackage


class Sbt(BinaryPackage):
    """Scala Build Tool"""

    homepage = "https://www.scala-sbt.org"
    url = "https://github.com/sbt/sbt/releases/download/v{version}/sbt-{version}.tgz"

    versions = [
        "1.10.0",
    ]
