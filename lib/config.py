import tomllib
from pathlib import Path


class Config:
    def __init__(self, path: Path):
        if not path.is_file():
            raise FileNotFoundError(f"Config file not found: {path}")

        with open(path, "rb") as f:
            data = tomllib.load(f)

        paths = data["paths"]

        self.software_root = Path(paths["software_root"])
        self.container_root = Path(paths["container_root"])

        self.apps = paths["apps_dir"]
        self.downloads = paths["downloads_dir"]
        self.builds = paths["builds_dir"]
        self.modulefiles = paths["modulefiles_dir"]
