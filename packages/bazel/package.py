from lib.dependency import Dependency
from lib.package import Package


class Bazel(Package):
    """Bazel is an open-source build and test tool similar to Make, Maven, and
    Gradle. It uses a human-readable, high-level build language. Bazel supports
    projects in multiple languages and builds outputs for multiple platforms.
    Bazel supports large codebases across multiple repositories, and large
    numbers of users."""

    homepage = "https://bazel.build/"
    url = "https://github.com/bazelbuild/bazel/releases/download/{version}/bazel-{version}-dist.zip"

    versions = [
        "7.4.1",
    ]

    depends_on = [
        Dependency("openjdk", type=("build", "run")),
    ]

    def module_env(self):
        return {
            "JAVA_HOME": str(self.dep("openjdk").prefix),
        }

    def build(self):
        self.run_cmd(
            ["bash", str(self.build_dir / "compile.sh")],
            cwd=self.build_dir,
            env={
                "EXTRA_BAZEL_ARGS": "--tool_java_runtime_version=local_jdk",
            },
        )

    def install(self):
        self.install_binary(self.build_dir / "output" / "bazel")
