from dataclasses import dataclass


@dataclass
class PackageSpec:
    name: str
    version: str | None = None


def parse_spec(spec: str) -> PackageSpec:
    if "@" in spec:
        name, version = spec.split("@", 1)
        return PackageSpec(name.strip(), version.strip())
    return PackageSpec(spec.strip())
