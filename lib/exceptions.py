class SDError(Exception):
    pass


class PackageNotFoundError(SDError):
    def __init__(self, name: str, required_by: str | None = None):
        msg = f"Package '{name}' not found"
        if required_by:
            msg += f" (required by '{required_by}')"
        super().__init__(msg)


class UndeclaredDependencyError(SDError):
    def __init__(self, package_name: str, dep_name: str):
        msg = f"Package '{package_name}' tried to use undeclared dependency '{dep_name}'"
        super().__init__(msg)
