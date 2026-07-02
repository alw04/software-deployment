import importlib.util
import sys
from pathlib import Path

from lib.exceptions import PackageNotFoundError

PACKAGE_REGISTRY = {}
_loaded = False


def register_package(cls):
    pkg_key = cls.__module__.rsplit(".", 1)[-1].lower()
    PACKAGE_REGISTRY[pkg_key] = cls
    return cls


def load_all_packages():
    global _loaded
    if _loaded:
        return

    packages_dir = Path(__file__).resolve().parents[1] / "packages"

    for pkg_dir in sorted(packages_dir.iterdir()):
        if not pkg_dir.is_dir():
            continue

        pkg_file = pkg_dir / "package.py"
        if not pkg_file.is_file():
            continue

        spec = importlib.util.spec_from_file_location(f"packages.{pkg_dir.name}", pkg_file)

        if spec is None or spec.loader is None:
            raise ImportError(f"Cannot load package: {pkg_dir.name}")

        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module

        try:
            spec.loader.exec_module(module)
        except Exception as e:
            raise ImportError(f"Failed to load package {pkg_dir.name!r}: {e}") from e

    _loaded = True


def get_package(name: str, *, required_by: str | None = None):
    load_all_packages()

    pkg_key = name.lower()
    if pkg_key not in PACKAGE_REGISTRY:
        raise PackageNotFoundError(name, required_by)

    return PACKAGE_REGISTRY[pkg_key]
