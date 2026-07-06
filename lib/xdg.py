from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(frozen=True)
class XdgDirs:
    config_dir: Path
    cache_dir: Path
    state_dir: Path
    data_dir: Path


def get_xdg_dirs(app_name: str) -> XdgDirs:
    home = Path.home()

    return XdgDirs(
        config_dir=Path(os.getenv("XDG_CONFIG_HOME", home / ".config")) / app_name,
        cache_dir=Path(os.getenv("XDG_CACHE_HOME", home / ".cache")) / app_name,
        state_dir=Path(os.getenv("XDG_STATE_HOME", home / ".local" / "state")) / app_name,
        data_dir=Path(os.getenv("XDG_DATA_HOME", home / ".local" / "share")) / app_name,
    )
