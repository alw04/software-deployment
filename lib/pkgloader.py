import importlib
import pkgutil

import recipes

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


def load_all_recipes():
    for module in pkgutil.iter_modules(recipes.__path__, recipes.__name__ + "."):
        importlib.import_module(module.name)


def get_package(name: str, *, required_by: str | None = None):
    if not PACKAGE_REGISTRY:
        load_all_recipes()

    pkg_key = name.lower()
    if pkg_key not in PACKAGE_REGISTRY:
        raise PackageNotFoundError(name, required_by)

    return PACKAGE_REGISTRY[pkg_key]
