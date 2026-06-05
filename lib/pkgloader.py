import importlib.util
from pathlib import Path

PACKAGE_REGISTRY = {}


class PackageNotFoundError(Exception):
    def __init__(self, name, required_by=None):
        msg = f"Package '{name}' not found"
        if required_by:
            msg += f" (required by '{required_by}')"
        super().__init__(msg)


def register_package(cls):
    PACKAGE_REGISTRY[cls.__name__.lower()] = cls
    return cls


def load_all_packages():
    packages_dir = Path(__file__).resolve().parents[1] / "packages"

    for pkg_dir in packages_dir.iterdir():
        if not pkg_dir.is_dir():
            continue

        pkg_file = pkg_dir / "package.py"
        if not pkg_file.is_file():
            continue

        spec = importlib.util.spec_from_file_location(f"packages.{pkg_dir.name}", pkg_file)

        if spec is None or spec.loader is None:
            raise ImportError(f"Cannot load package: {pkg_dir.name}")

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)


def get_package(name: str, *, required_by: str | None = None):
    if not PACKAGE_REGISTRY:
        load_all_packages()

    pkg_key = name.lower()
    if pkg_key not in PACKAGE_REGISTRY:
        raise PackageNotFoundError(name, required_by)

    return PACKAGE_REGISTRY[pkg_key]
