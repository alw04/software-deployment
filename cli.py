import argparse
from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent

from jinja2 import Environment, FileSystemLoader

from lib.config import Config
from lib.package import Package
from lib.pkgloader import PACKAGE_REGISTRY, get_package, load_all_recipes


@dataclass
class PackageSpec:
    name: str
    version: str | None = None


class Context:
    def __init__(self, config: Config, args: argparse.Namespace):
        self.config = config
        self.args = args

        TEMPLATE_DIR = Path(__file__).resolve().parent / "lib" / "templates"
        self.jinja_env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), trim_blocks=True, lstrip_blocks=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="cli.py",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=dedent(
            """\
            Examples:
                # Install individual packages
                python3 cli.py install python
                python3 cli.py install python r gcc@15.2.0

                # Install from groups
                python3 cli.py install --group common
                python3 cli.py install --group common --group sequence_tools

                # Mix packages and groups
                python3 cli.py install python --group common
                python3 cli.py install python gcc --group common --group sequence_tools

                # Force rebuild
                python3 cli.py install python --force
                python3 cli.py install python --group common --force

                # Dry run (show what would be installed)
                python3 cli.py install python gcc --dry-run
                python3 cli.py install --group common --dry-run

                # List available packages
                python3 cli.py list
                python3 cli.py list --group common
                python3 cli.py list --group common --group sequence_tools

                # Show package info
                python3 cli.py info python
                python3 cli.py info python@3.14.0
            """
        ),
    )

    parser.add_argument("--config", default="config.toml", type=Path, metavar="PATH", help="Path to config file")

    subparser = parser.add_subparsers(dest="command", required=True)

    install_parser = subparser.add_parser(
        "install", help="Install one or more packages", description="Install packages and their dependencies"
    )
    install_parser.add_argument(
        "packages",
        nargs="+",
        metavar="package[@version]",
        help="Package(s) to install (e.g. python gcc@15.2.0)",
    )
    install_parser.add_argument(
        "-g",
        "--group",
        action="append",
        metavar="GROUP",
        help="Install a predefined group of packages (e.g. common, sequence_tools)",
    )
    install_parser.add_argument("-f", "--force", action="store_true", help="Force rebuild even if already installed")
    install_parser.add_argument("--dry-run", action="store_true", help="Show what would be installed without executing")
    install_parser.set_defaults(handler=cmd_install)

    list_parser = subparser.add_parser(
        "list",
        help="List available packages in the registry",
        description="Show available packages in the registry",
    )
    list_parser.add_argument(
        "--group", action="append", metavar="GROUP", help="Filter packages by group (e.g. common, sequence_tools)"
    )
    list_parser.set_defaults(handler=cmd_list)

    info_parser = subparser.add_parser(
        "info",
        help="Show package details",
        description="Display metadata about a package including versions, description, and homepage",
    )
    info_parser.add_argument("package", metavar="package[@version]", help="Package to inspect (e.g. r or r@4.5.1)")
    info_parser.set_defaults(handler=cmd_info)

    return parser.parse_args()


def parse_spec(spec: str) -> PackageSpec:
    if "@" in spec:
        name, version = spec.split("@", 1)
        return PackageSpec(name.strip(), version.strip())
    return PackageSpec(spec.strip())


def install_package(pkg: Package, installed: dict):
    key = (pkg.name, pkg.version)

    if key in installed:
        return installed[key]

    installed[key] = pkg

    for dep in pkg.depends_on:
        dep_cls = get_package(dep.name, required_by=pkg.name)

        dep_pkg = dep_cls(dep.version, pkg.ctx)

        install_package(dep_pkg, installed)

        pkg.dependencies[dep.name] = dep_pkg

    pkg.run()


def cmd_install(ctx: Context):
    installed = {}

    for package in ctx.args.packages:
        spec = parse_spec(package)

        pkg_cls = get_package(spec.name)
        pkg = pkg_cls(spec.version, ctx)

        install_package(pkg, installed)


def cmd_list(ctx: Context):
    if not PACKAGE_REGISTRY:
        load_all_recipes()

    if not PACKAGE_REGISTRY:
        print("No packages found in the registry.")
        return

    for pkg_name, pkg_cls in sorted(PACKAGE_REGISTRY.items()):
        try:
            pkg_version = pkg_cls.default_version()
        except ValueError:
            pkg_version = "undefined"

        print(pkg_name, pkg_version)


def cmd_info(ctx: Context):
    spec = parse_spec(ctx.args.package)
    pkg_cls = get_package(spec.name)
    pkg = pkg_cls(spec.version, ctx)

    INDENT = "    "

    description = pkg.description.replace("\n", f"\n{INDENT}")
    versions = "\n".join(f"{INDENT}{v}" for v in pkg_cls.versions)
    deps = "\n".join(f"{INDENT}{d.name}" for d in pkg_cls.depends_on) if pkg_cls.depends_on else f"{INDENT}(none)"

    output = f"""\
Package: {pkg.name}

Description:
    {description}

Homepage: {pkg_cls.homepage}

Default Version:
    {pkg_cls.default_version()}

Versions:
{versions}

Dependencies:
{deps}
"""

    print(output)


def main():
    args = parse_args()
    config = Config(args.config)

    ctx = Context(config, args)

    args.handler(ctx)


if __name__ == "__main__":
    main()
