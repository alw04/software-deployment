import os
import tomllib
from pathlib import Path


def expand_path(value: str) -> Path:
    expanded = os.path.expandvars(value)

    if "$" in expanded:
        raise ValueError(f"Unexpanded environment variable in path: {value}")

    return Path(expanded).expanduser()


class Config:
    APPS_DIR = "apps"
    DOWNLOADS_DIR = "downloads"
    BUILDS_DIR = "builds"
    MODULEFILES_DIR = "modulefiles"

    IMAGES_DIR = "images"

    def __init__(self, path: Path):
        if not path.is_file():
            raise FileNotFoundError(f"Config file not found: {path}")

        with open(path, "rb") as f:
            data = tomllib.load(f)

        paths = data.get("paths")
        if not isinstance(paths, dict):
            raise ValueError("Missing required [paths] section")

        required_paths = ("software_root", "container_root")
        for key in required_paths:
            value = paths.get(key)

            if value is None:
                raise ValueError(f"Missing required paths.{key}")

            if not isinstance(value, str):
                raise ValueError(f"paths.{key} must be a string")

        self.software_root = expand_path(paths["software_root"])
        self.container_root = expand_path(paths["container_root"])

        build = data.get("build", {})
        jobs = build.get("jobs")

        if jobs is None:
            jobs = os.cpu_count() or 1
        elif not isinstance(jobs, int) or jobs < 1:
            raise ValueError(
                f"build.jobs must be an integer >= 1 (got {jobs!r}). Omit it to use automatic CPU-based selection."
            )

        self.jobs = jobs
