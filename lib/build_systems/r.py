import shutil
from pathlib import Path

import requests

from lib.dependency import Dependency
from lib.package import Package


class RPackage(Package):
    abstract = True

    cran: str | None = None

    @property
    def cran_cache_dir(self) -> Path:
        return self.ctx.cache_dir / "cran"

    @property
    def cran_packages_file(self) -> Path:
        return self.cran_cache_dir / "PACKAGES"

    @property
    def cran_packages_etag_file(self) -> Path:
        return self.cran_cache_dir / "PACKAGES.etag"

    def _download_cran_index(self):
        self.cran_cache_dir.mkdir(parents=True, exist_ok=True)

        headers = {}

        if self.cran_packages_etag_file.exists():
            headers["If-None-Match"] = self.cran_packages_etag_file.read_text().strip()

        r = requests.get("https://cran.r-project.org/src/contrib/PACKAGES", headers=headers)
        r.raise_for_status()

        if r.status_code == 304:
            return

        self.cran_packages_file.write_text(r.text)

        if etag := r.headers.get("ETag"):
            self.cran_packages_etag_file.write_text(etag)

    def _latest_cran_version(self) -> str:
        self._download_cran_index()

        current_pkg = None

        for line in self.cran_packages_file.read_text().splitlines():
            if line.startswith("Package: "):
                current_pkg = line.removeprefix("Package: ")
            elif current_pkg == self.cran and line.startswith("Version: "):
                return line.removeprefix("Version: ")

        raise ValueError(f"Package {self.cran!r} not found in CRAN index")

    def url_for_version(self, version) -> str:
        if self.cran is None:
            return super().url_for_version(version)

        latest = self._latest_cran_version()

        if version == latest:
            return f"https://cran.r-project.org/src/contrib/{self.cran}_{self.version}.tar.gz"

        return f"https://cran.r-project.org/src/contrib/Archive/{self.cran}/{self.cran}_{self.version}.tar.gz"

    phases = (
        "download",
        "extract",
        "install",
    )

    depends_on = [
        Dependency("r", type=("build", "run")),
    ]

    @property
    def libdir(self):
        return self.prefix / "lib" / "R" / "library"

    @property
    def r_lib(self):
        return {
            "R_LIBS_USER": [self.libdir],
        }

    def additional_build_env(self):
        return self.r_lib

    def modulefile_prepend_path(self):
        return self.r_lib

    @property
    def r(self):
        return self.dep("r").prefix / "bin" / "R"

    def install(self):
        tmp_dir = self.prefix / ".library.tmp"
        shutil.rmtree(tmp_dir, ignore_errors=True)
        tmp_dir.mkdir(parents=True, exist_ok=True)

        try:
            self.run_cmd([str(self.r), "CMD", "INSTALL", f"--library={tmp_dir}", "."], cwd=self.build_dir)

            shutil.rmtree(self.libdir, ignore_errors=True)
            self.libdir.parent.mkdir(parents=True, exist_ok=True)

            tmp_dir.replace(self.libdir)

        finally:
            shutil.rmtree(tmp_dir, ignore_errors=True)
