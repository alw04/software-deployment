from dataclasses import dataclass

from lib.spec import PackageSpec, parse_spec


@dataclass
class Dependency:
    spec: str
    type: str | tuple[str, ...] = "link"

    @property
    def package_spec(self) -> PackageSpec:
        return parse_spec(self.spec)

    @property
    def name(self) -> str:
        return self.package_spec.name

    @property
    def version(self) -> str | None:
        return self.package_spec.version

    @property
    def types(self) -> tuple[str, ...]:
        if isinstance(self.type, str):
            return (self.type,)
        return self.type
