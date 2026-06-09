from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Apptainer(AutotoolsPackage):
    """Apptainer is an open source container platform designed to be simple, fast, and
    secure. Many container platforms are available, but Apptainer is designed for
    ease-of-use on shared systems and in high performance computing (HPC)
    environments.
    """

    homepage = "https://apptainer.org"
    url = "https://github.com/apptainer/apptainer/releases/download/v{version}/apptainer-{version}.tar.gz"

    versions = [
        "1.4.1",
    ]

    depends_on = [
        Dependency("go", type="build"),
        Dependency("gocryptfs"),
        Dependency("squashfuse"),
    ]

    def configure(self):
        self.run_cmd(
            [
                "./mconfig",
                f"--prefix={self.prefix}",
                "--localstatedir=/var",
                f"--sysconfdir={self.prefix}/etc",
                "--with-suid",
            ],
            cwd=self.build_dir,
        )

    def build(self):
        self.run_cmd(["make", "-C", "./builddir"], cwd=self.build_dir)

    def install(self):
        self.run_cmd(["make", "-C", "./builddir", "install"], cwd=self.build_dir)
