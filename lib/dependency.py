from dataclasses import dataclass
from typing import TYPE_CHECKING

from lib.spec import parse_spec

if TYPE_CHECKING:
    from lib.package import Package


@dataclass
class Dependency:
    spec: str
    type: str | tuple[str, ...] = "link"
    when: str | tuple[str, ...] | None = None

    def __post_init__(self):
        if parse_spec(self.spec).all_versions:
            raise ValueError(
                f"Dependency({self.spec!r}): '@all'/'@*' can only be used as a CLI version selector, not as a dependency pin.\nEither omit the version to use the dependency's default version, or pin a specific version."
            )

    @property
    def name(self) -> str:
        return parse_spec(self.spec).name

    @property
    def version(self) -> str | None:
        return parse_spec(self.spec).version

    @property
    def types(self) -> tuple[str, ...]:
        if isinstance(self.type, str):
            return (self.type,)
        return self.type

    def applies_to(self, pkg: Package) -> bool:
        if self.when is None:
            return True

        if isinstance(self.when, str):
            return pkg.version == self.when

        return pkg.version in self.when
