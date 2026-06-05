import shutil

from lib.package import Package


class BinaryPackage(Package):
    abstract = True

    phases = (
        "download",
        "extract",
        "install",
    )

    def install(self):
        shutil.copytree(self.build_dir, self.prefix, dirs_exist_ok=True)
