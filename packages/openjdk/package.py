from lib.build_systems.binary import BinaryPackage


class Openjdk(BinaryPackage):
    """The free and opensource java implementation"""

    homepage = "https://openjdk.org/"

    urls_by_version = {
        "17": "https://github.com/adoptium/temurin17-binaries/releases/download/jdk-17.0.19%2B10/OpenJDK17U-jdk_x64_linux_hotspot_17.0.19_10.tar.gz",
        "21": "https://github.com/adoptium/temurin21-binaries/releases/download/jdk-21.0.9%2B10/OpenJDK21U-jdk_x64_linux_hotspot_21.0.9_10.tar.gz",
    }

    versions = [
        "21",
        "17",
    ]

    def module_env(self):
        return {
            "JAVA_HOME": str(self.prefix),
        }
