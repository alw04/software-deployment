from lib.dependency import Dependency
from lib.package import Package


class PerlPackage(Package):
    abstract = True

    phases = (
        "download",
        "extract",
        "build",
        "install",
    )

    depends_on = [
        Dependency("perl", type=("build", "run")),
    ]

    @property
    def perl_lib(self):
        return {
            "PERL5LIB": [self.prefix / "lib" / "perl5"],
        }

    def additional_build_env(self):
        return self.perl_lib

    def modulefile_prepend_path(self):
        return self.perl_lib

    @property
    def perl(self):
        return self.dep("perl").prefix / "bin" / "perl"

    def build(self):
        if (self.build_dir / "Makefile.PL").is_file():
            self.run_cmd([str(self.perl), "Makefile.PL", f"INSTALL_BASE={self.prefix}"], cwd=self.build_dir)
            self.run_cmd(["make", f"-j{self.build_jobs}"], cwd=self.build_dir)

        elif (self.build_dir / "Build.PL").is_file():
            self.run_cmd([str(self.perl), "Build.PL", f"--install_base={self.prefix}"], cwd=self.build_dir)
            self.run_cmd(["./Build"], cwd=self.build_dir)

        else:
            raise RuntimeError(f"{self.name}@{self.version}: Unsupported Perl build system")

    def install(self):
        if (self.build_dir / "Makefile").is_file():
            self.run_cmd(["make", "install"], cwd=self.build_dir)
        else:
            self.run_cmd(["./Build", "install"], cwd=self.build_dir)
