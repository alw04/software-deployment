from pathlib import Path

from lib.dependency import Dependency
from lib.package import Package


class ContainerPackage(Package):
    abstract = True

    image: str | None = None

    phases = ("pull",)

    depends_on = [
        Dependency("apptainer", type="run"),
    ]

    @property
    def root(self) -> Path:
        return self.ctx.config.container_root

    @property
    def prefix(self) -> Path:
        return self.root / self.ctx.config.IMAGES_DIR / self.name / self.version

    @property
    def image_path(self) -> Path:
        return self.prefix / f"{self.name}_{self.version}.sif"

    def format_shell_command(self, cmd: str) -> str:
        return f"apptainer exec {self.image_path} {cmd}"

    def image_for_version(self, version: str) -> str:
        if self.image:
            return self.image.format(version=version)

        raise NotImplementedError(f"{self.name}: no image defined")

    def pull(self):
        image_ref = self.image_for_version(self.version)

        self.image_path.parent.mkdir(parents=True, exist_ok=True)

        if self.image_path.is_file() and not self.ctx.args.force:
            self.log.info("skipping pull, image already exists: %s", self.image_path)
            return

        self.log.info("pulling container image: %s -> %s", image_ref, self.image_path)

        tmp_image = self.image_path.with_name(self.image_path.name + ".tmp")

        cmd = ["apptainer", "pull"]

        cmd += [str(tmp_image), image_ref]

        try:
            self.run_cmd(cmd)
            tmp_image.replace(self.image_path)
            self.log.info("container pull complete")
        except Exception:
            if tmp_image.exists():
                tmp_image.unlink()
            raise
