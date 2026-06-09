from lib.package import Package


class ContainerPackage(Package):
    abstract = True

    phases = (
        "pull",
        "install",
    )

    @property
    def root(self):
        return self.ctx.config.container_root

    @property
    def prefix(self):
        return self.root / self.ctx.config.apps_dir / self.name / self.version

    @property
    def modulefile(self):
        return self.root / self.ctx.config.modulefiles_dir / self.name / f"{self.version}.lua"
