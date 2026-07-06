import argparse
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from lib.config import Config
from lib.term import TermInfo
from lib.xdg import XdgDirs


class Context:
    def __init__(self, args: argparse.Namespace, app_root: Path, xdg: XdgDirs, config: Config, term: TermInfo):
        self.args = args
        self.app_root = app_root
        self.xdg = xdg
        self.config = config
        self.term = term

        self.jinja_env = Environment(
            loader=FileSystemLoader(
                [
                    self.app_root / "lib" / "templates",
                    self.app_root / "packages",
                ]
            ),
            trim_blocks=True,
            lstrip_blocks=True,
        )
