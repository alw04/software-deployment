from lib.package import Package


class Boost(Package):
    """Boost provides free peer-reviewed portable C++ source
    libraries, emphasizing libraries that work well with the C++
    Standard Library.

    Boost libraries are intended to be widely useful, and usable
    across a broad spectrum of applications. The Boost license
    encourages both commercial and non-commercial use.
    """

    homepage = "https://www.boost.org"

    def url_for_version(self, version):
        version_underscored = version.replace(".", "_")
        return f"https://downloads.sourceforge.net/project/boost/boost/{version}/boost_{version_underscored}.tar.bz2"

    versions = [
        "1.88.0",
    ]

    def configure(self):
        self.run_cmd(["./bootstrap.sh", f"--prefix={self.prefix}"], cwd=self.build_dir)

    def build(self):
        self.run_cmd(["./b2", f"-j{self.build_jobs()}"], cwd=self.build_dir)

    def install(self):
        self.run_cmd(["./b2", "install", f"--prefix={self.prefix}"], cwd=self.build_dir)
