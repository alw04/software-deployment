from lib.build_systems.binary import BinaryPackage
from lib.dependency import Dependency


class Bazel(BinaryPackage):
    """Bazel is an open-source build and test tool similar to Make, Maven, and
    Gradle. It uses a human-readable, high-level build language. Bazel supports
    projects in multiple languages and builds outputs for multiple platforms.
    Bazel supports large codebases across multiple repositories, and large
    numbers of users."""

    homepage = "https://bazel.build/"
    url = "https://github.com/bazelbuild/bazel/releases/download/{version}/bazel-{version}-linux-x86_64"

    versions = [
        "9.1.1",
        "7.4.1",
    ]

    depends_on = [
        Dependency("openjdk", type="run"),
    ]

    def module_env(self):
        return {
            "JAVA_HOME": str(self.dep("openjdk").prefix),
        }

    def install(self):
        self.install_binary(self.download_file, name="bazel")
