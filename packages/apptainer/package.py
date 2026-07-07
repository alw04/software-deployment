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

    def apply_toolchain_env(self):
        super().apply_toolchain_env()

        gopath = self.build_dir / ".gopath"
        gomodcache = self.build_dir / ".gomodcache"
        gocache = self.build_dir / ".gocache"
        for d in (gopath, gomodcache, gocache):
            d.mkdir(parents=True, exist_ok=True)
        self.env.update(
            {
                "GOPATH": str(gopath),
                "GOMODCACHE": str(gomodcache),
                "GOCACHE": str(gocache),
            }
        )

    def configure(self):
        self.run_cmd(
            [
                str(self.build_dir / "mconfig"),
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

        libexec_bin = self.prefix / "libexec" / "apptainer" / "bin"

        self.install_file(self.dep("gocryptfs").prefix / "bin" / "gocryptfs", libexec_bin / "gocryptfs", mode=0o755)
        self.install_file(
            self.dep("squashfuse").prefix / "bin" / "squashfuse_ll", libexec_bin / "squashfuse_ll", mode=0o755
        )
