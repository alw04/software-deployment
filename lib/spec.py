from dataclasses import dataclass


@dataclass
class PackageSpec:
    name: str
    version: str | None = None
    all_versions: bool = False


def parse_spec(spec: str) -> PackageSpec:
    spec = spec.strip()

    if "@" in spec:
        name, version = spec.split("@", 1)
        name = name.strip()
        version = version.strip()

        if version in ("*", "all"):
            return PackageSpec(name=name, version=None, all_versions=True)

        return PackageSpec(name=name, version=version)

    return PackageSpec(name=spec)
