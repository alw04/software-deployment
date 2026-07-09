# Software Deployment

A source-based software deployment system for building software, installing containers, and generating modulefiles for shared computing environments.

> **Note:** This project is a work in progress. Some features and behavior are subject to change as development continues.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
    - [Paths](#paths)
    - [Build Settings](#build-settings)
- [Directory Layout](#directory-layout)
- [Usage](#usage)
    - [Package versions](#package-versions)
    - [install](#install)
    - [uninstall](#uninstall)
    - [list](#list)
    - [info](#info)
    - [modules regenerate](#modules-regenerate)
- [Writing Packages](#writing-packages)
    - [Minimal Example](#minimal-example)
    - [Package class reference](#package-class-reference)
        - [Class attributes](#class-attributes)
        - [Properties](#properties)
        - [Overridable methods](#overridable-methods)
        - [Helper methods](#helper-methods)
    - [Build systems](#build-systems)
        - [AutotoolsPackage](#autotoolspackage)
        - [CMakePackage](#cmakepackage)
        - [MakefilePackage](#makefilepackage)
        - [MesonPackage](#mesonpackage)
        - [GoPackage](#gopackage)
        - [PythonPackage](#pythonpackage)
        - [PythonSourcePackage](#pythonsourcepackage)
        - [PerlPackage](#perlpackage)
        - [RPackage](#rpackage)
        - [BinaryPackage](#binarypackage)
    - [Dependencies](#dependencies)
    - [Generated modulefiles](#generated-modulefiles)
- [Using modulefiles](#using-modulefiles)

## Requirements

- Python 3.11+
- A Unix-like operating system
- A compiler/toolchain environment for building source packages
- Lmod (for using generated modulefiles)

## Installation

Clone the repository:

```bash
git clone https://github.com/alw04/software-deployment.git
cd software-deployment
```

Install the Python dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Verify the installation:

```bash
./sd --help
```

## Configuration

`sd` uses a TOML configuration file to control installation locations and build settings.

By default, `sd` looks for a configuration file at:

```text
config.toml
```

A custom configuration file can be specified with:

```bash
sd --config path/to/config.toml <command>
```

Example configuration:

```toml
[paths]
# Root directory for installed software, source downloads, build directories, and generated modulefiles.
software_root = "path/to/software"

# Root directory for Apptainer/Singularity container images and generated modulefiles.
container_root = "path/to/containers"

[build]
# Number of parallel jobs for builds. If omitted, uses all available CPUs.
# jobs = 8
```

### Paths

Both `paths.software_root` and `paths.container_root` are required.

Paths may be absolute or relative. Relative paths are resolved from the current working directory. Paths support environment variable expansion and `~` expansion for the user's home directory.

### Build Settings

`jobs` controls the maximum number of parallel jobs used during builds. If not specified, `sd` automatically uses all available CPUs.

## Directory Layout

`sd` organizes software by package name and version underneath the configured `software_root`.

The software root contains installed packages, build files, source downloads, and generated modulefiles.

For example, installing GCC may create a layout like this:

```text
software_root/
├── apps/
│   └── gcc/
│       └── 15.2.0/
│           ├── bin/
│           ├── include/
│           ├── lib/
│           └── ...
├── downloads/
│   └── gcc/
│       └── 15.2.0/
│           └── gcc-15.2.0.tar.gz
├── builds/
│   └── gcc/
│       └── 15.2.0/
└── modulefiles/
    └── gcc/
        └── 15.2.0.lua
```

Container images are stored separately underneath the configured `container_root`.

For example:

```text
container_root/
├── images/
│   └── gcc/
│       └── 15.2.0/
│           └── gcc_15.2.0.sif
└── modulefiles/
    └── gcc/
        └── 15.2.0.lua
```

## Usage

```text
sd [--config PATH] <command> [options]
```

### Package versions

Package names may optionally include a version.

```bash
# Default version
gcc

# Specific version
gcc@15.2.0

# All versions
gcc@all
```

When no version is specified, the package's default version is used. `@all` (or `@*`) selects all available versions of the package.

Additional version selector forms may be added in the future.

### install

Build and install one or more packages and their dependencies.

If a selected package it already installed, it is skipped. Use `-f/--force` to rebuild the package, or `-ff/--force-deps` to rebuild the package and all of its dependencies.

```bash
# Install the default version of a package
sd install python

# Install a specific version
sd install gcc@15.2.0

# Install multiple packages
sd install python gcc@15.2.0

# Preview the install plan without installing anything
sd install repeatmodeler --dry-run

# Force rebuild if already installed
sd install repeatmodeler -f

# Force rebuild of the package and all its dependencies
sd install repeatmodeler -ff
```

### uninstall

Remove installed packages and their generated modulefiles.

```bash
# Uninstall a package
sd uninstall python

# Uninstall a specific version
sd uninstall gcc@15.2.0

# Uninstall multiple packages
sd uninstall python gcc@15.2.0

# Preview what would be removed
sd uninstall tmux --dry-run

# Remove cached downloads and build directories as well
sd uninstall tmux --purge

# Skip the confirmation prompt
sd uninstall tmux --yes
```

> Note: `uninstall` does not check whether other installed packages still depend on the package being removed. Removing a package may affect other installed packages that depend on it.

### list

List all packages registered in the registry.

```bash
sd list
```

### info

Display metadata for a package, including its description, homepage, available versions, default version, and declared dependencies.

```bash
sd info gcc
```

### modules regenerate

Regenerate modulefiles for installed packages without rebuilding them. Useful after changing a modulefile template or package metadata.

```bash
# Regenerate for all installed packages
sd modules regenerate --all

# Regenerate for specific packages
sd modules regenerate python gcc@15.2.0

# Preview without writing
sd modules regenerate --all --dry-run
```

## Writing Packages

Packages are Python classes stored at `packages/<name>/package.py`. Packages are discovered and registered automatically at startup.

The package name is derived from the package directory name, lowercased.

### Minimal Example

```python
# packages/zlib/package.py
from lib.build_systems.autotools import AutotoolsPackage

class Zlib(AutotoolsPackage):
    """A free, general-purpose, legally unencumbered lossless
    data-compression library.
    """

    homepage = "https://zlib.net"
    url = "http://zlib.net/fossils/zlib-{version}.tar.gz"

    versions = [
        "1.3.1",
    ]
```

This is a complete, functional package. `AutotoolsPackage` provides the standard download, extract, configure, build, and install phases, and the package generates its modulefile after installation.

### Package class reference

Every package subclasses `Package` or one of the built-in build-system classes. Packages are configured through class attributes and can customize behavior by overriding methods when needed. The class docstring is used as the package description.

> Note: This reference documents the parts of the package API intended for package definitions. Some internal attributes and methods are intentionally omitted.

#### Class attributes

Attributes defined on the package class to configure the package.

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `homepage` | `str \| None` | `None` | Project homepage URL. |
| `url` | `str \| None ` | `None` | Download URL template. `{version}` is substituted at download time. |
| `urls_by_version` | `dict[str, str] \| None` | `None` | Per-version download URLs, for packages that don't follow a consistent URL scheme. Takes priority over `url`. |
| `versions` | `list[str]` | `[]` | List of supported versions. The first entry is the default version when no `@<version>` is provided. |
| `max_jobs` | `int \| None` | `None` | Package-specific parallel job limit. The lower of `max_jobs` and the global `build.jobs` setting is used. |
| `depends_on` | `list[Dependency]` | `[]` | Dependencies required by this package. |
| `conflicts` | `list[str]` | `[]` | Modules that cannot be loaded alongside this package. |
| `shell_functions` | `dict[str, str]` | `{}` | Shell functions to expose in the generated modulefile. |
| `source_subdir` | `str` | `"."` | Subdirectory within the extracted archive that contains the actual source. Useful for packages that nest their source inside a subdirectory. |
| `download_headers` | `dict[str, str]` | `{}` | Additional HTTP headers to send when downloading source archives. |
| `link_libs` | `list[str]` | `[]` | Additional libraries to link against (without the `-l` prefix) during the build. |
| `phases` | `tuple[str, ...]` | `("download", "extract", "configure", "build", "install")` | Build phases executed for the package. Override for packages with a custom build flow. |
| `abstract` | `bool` | `False` | If `True`, prevents the class from being registered in the package registry. Used for base classes and build-system classes. |

#### Properties

Values available when a package is being built or installed.

| Property | Type | Description |
|----------|------|-------------|
| `name` | `str` | Package name derived from the package directory name. |
| `version` | `str` | Version this package instance was constructed with. |
| `prefix` | `Path` | Installation prefix. |
| `build_path` | `Path` | Directory used for build files. |
| `build_dir` | `Path` | Source directory used during the build (`build_path / source_subdir`). |
| `download_file` | `Path` | Path to the downloaded source file. |
| `build_jobs` | `int` | Number of parallel build jobs. |
| `build_dependencies` | `list[Package]` | Resolved dependencies of type `"build"`. |
| `link_dependencies` | `list[Package]` | Resolved dependencies of type `"link"`. |
| `run_dependencies` | `list[Package]` | Resolved dependencies of type `"run"`. |

#### Overridable methods

Packages can override these methods to customize package behavior.

| Method | Description |
|--------|-------------|
| `url_for_version(version: str) -> str` | Return the download URL for a version. By default, uses `urls_by_version` or substitutes `{version}` in `url`. Override for custom URL resolution. |
| `additional_build_env() -> dict[str, list[Path]]` | Return additional environment variables required from dependencies during the build. Empty by default. |
| `apply_toolchain_env()` | Apply toolchain-related environment changes. No-op by default. |
| `configure()` | Configure the package. No-op by default. |
| `build()` | Build the package. No-op by default. |
| `install()` | Install the package. Raises `NotImplementedError` by default.
| `modulefile_prepend_path() -> dict[str, list[Path]]` | Return additional paths to prepend to the generated modulefile. Empty by default. |
| `modulefile_setenv() -> dict[str, str]` | Return environment variables to set in the generated modulefile. Empty by default. |

#### Helper methods

The following methods are available to package definitions for common tasks.

| Method | Description |
|--------|-------------|
| `dep(name: str) -> Package` | Retrieve a resolved dependency by name. |
| `run_cmd(args: list[str], cwd=None, env=None, input=None)` | Execute a command during a phase, optionally provide a working directory, environment, or stdin input. |
| `install_file(src: str \| Path, dst: str \| Path, mode=None)` | Install a file to the specified destination path. Creates parent directories as needed. |
| `install_binary(src: str \| Path, name=None)` | Install a binary into `prefix/bin`, optionally using a different filename. |
| `install_symlink(target: str \| Path, link: str \| Path)` | Create a symbolic link at the specified path. Creates parent directories as needed. |
| `install_directory(src: str \| Path, dst: str \| Path)` | Install a directory recursively to the specified destination path. |
| `append_env(key: str, value: str, sep=" ")` | Append a value to a package environment variable, creating it if it does not already exist. |
| `prepend_env(key: str, value: str, sep=" ")` | Prepend a value to a package environment variable, creating it if it does not already exist. |

### Build systems

Build-system classes implement common build workflows. Packages typically inherit from one of the built-in build-system classes and only need to define package-specific metadata and customization when necessary.

Not every package will fit perfectly into an existing build system. If a build system is close but requires additional behavior, packages can override the provided methods to customize the workflow. To extend the existing behavior, call the parent implementation with `super()` and add package-specific logic before or after it as needed.

For packages that do not match any built-in build-system class, subclass `Package` directly and implement the required behavior.

#### AutotoolsPackage

Provides a standard Autotools build flow.

Phases:

```text
download → extract → configure → build → install
```

Implements the following methods:

| Method | Behavior |
|--------|----------|
| `apply_toolchain_env()` | Adds dependency include paths to `CPPFLAGS`, library paths to `LDFLAGS`, pkg-config paths to `PKG_CONFIG_PATH` and libraries from `link_libs` to `LDLIBS`. |
| `configure()` | Runs `./configure --prefix=<package prefix>` with additional arguments from `configure_args()`. If the script does not exist, attempts to generate it using `autogen.sh` or `autoreconf -fi`. |
| `build()` | Runs `make -j<build_jobs>` with additional arguments from `make_args()`. |
| `install()` | Runs `make install` with additional arguments from `install_args()`. |

Additional customization methods:

| Method | Description |
|--------|-------------|
| `configure_args() -> list[str]` | Additional arguments passed to `./configure`. |
| `make_args() -> list[str]` | Additional arguments passed to `make`. |
| `install_args() -> list[str]` | Additional arguments passed to `make install`. |

---

#### CMakePackage

Provides a standard CMake build flow.

Automatically adds the `cmake` build dependency.

Phases:

```text
download → extract → configure → build → install
```

Implements the following methods:

| Method | Behavior |
|--------|----------|
| `apply_toolchain_env()` | Adds dependency prefixes to `CMAKE_PREFIX_PATH`, include paths to `CMAKE_INCLUDE_PATH`, library paths to `CMAKE_LIBRARY_PATH`, pkg-config paths to `PKG_CONFIG_PATH`, and libraries from `link_libs` to `LDFLAGS`. |
| `configure()` | Runs `cmake -S <source> -B <build> -DCMAKE_INSTALL_PREFIX=<package prefix>` with additional arguments from `cmake_args()`. |
| `build()` | Runs `cmake --build <build directory> --parallel <build_jobs>`.
| `install()` | Runs `cmake --install <build directory>`. |
| `modulefile_prepend_path()` | Adds the package prefix to `CMAKE_PREFIX_PATH` in the generated modulefile. |

Additional customization methods:

| Method | Description |
|--------|-------------|
| `cmake_args() -> list[str]` | Additional arguments passed to `cmake` during configuration. |

---

#### MakefilePackage

Provides a standard Makefile-based build flow.

Phases:

```text
download → extract → configure → build → install
```

> Note: The `configure` phase is a no-op by default and can be overridden by packages that require additional configuration before building.

Implements the following methods:

| Method | Behavior |
|--------|----------|
| `apply_toolchain_env()` | Adds dependency include paths to `CPPFLAGS`, library paths to `LDFLAGS`, pkg-config paths to `PKG_CONFIG_PATH` and libraries from `link_libs` to `LDLIBS`. |
| `build()` | Runs `make -j<build_jobs>` with additional arguments from `make_args()`. |
| `install()` | Runs `make install` with additional arguments from `install_args()`. |

Additional customization methods:

| Method | Description |
|--------|-------------|
| `make_args() -> list[str]` | Additional arguments passed to `make`. |
| `install_args() -> list[str]` | Additional arguments passed to `make install`. |

---

#### MesonPackage

Provides a standard Meson build flow.

Automatically adds the `meson` and `ninja` build dependencies.

Phases:

```text
download → extract → configure → build → install
```

Implements the following methods:

| Method | Behavior |
|--------|----------|
| `apply_toolchain_env()` | Adds dependency include paths to `CFLAGS`, library paths to `LDFLAGS`, pkg-config paths to `PKG_CONFIG_PATH`, and libraries from `link_libs` to `LDFLAGS`. |
| `configure()` | Runs `meson setup <build directory> <source directory> --prefix=<package prefix>` with additional arguments from `meson_args()`. |
| `build()` | Runs `meson compile -C <build directory>`. |
| `install()` | Runs `meson install -C <build directory>`. |

Additional customization methods:

| Method | Description |
|--------|-------------|
| `meson_args() -> list[str]` | Additional arguments passed to `meson setup` during configuraton. |

---

#### GoPackage

Provides a standard Go build flow.

Automatically adds the `go` build dependency.

Phases:

```text
download → extract → build → install
```

Implements the following methods:

| Method | Behavior |
|--------|----------|
| `apply_toolchain_env()` | Sets isolated `GOPATH`, `GOMODCACHE`, and `GOCACHE` directories inside the build directory. |
| `build()` | Runs `go build -o <package name> <source directory>`. |
| `install()` | Installs the generated binary into `prefix/bin`. |

---

#### PythonPackage

Provides a Python virtual environment-based installation flow.

Automatically adds the `python` build dependency.

Phases:

```text
install
```

Implements the following methods:

| Method | Behavior |
|--------|----------|
| `additional_build_env()` | Adds the package's Python site-packages directory to `PYTHONPATH` for dependent packages during builds. |
| `modulefile_prepend_path()` | Adds the package's Python site-packages directory to `PYTHONPATH` in the generated modulefile. |
| `install()` | Creates a virtual environment in the package prefix and installs the package using `pip install <package>==<version>`. |

Additional properties:

| Property | Description |
|----------|-------------|
| `venv_python` | Path to the Python executable inside the package virtual environment. |

---

#### PythonSourcePackage

Extends `PythonPackage` with source archive support.

Phases:

```text
download → extract → install
```

Overrides the following methods from `PythonPackage`:

| Method | Behavior |
|--------|----------|
| `install()` | Creates a virtual environment in the package prefix and runs `pip install <source directory>`.

---

#### PerlPackage

Provides a standard Perl module build flow.

Automatically adds the `perl` build and runtime dependency.

Phases:

```text
download → extract → build → install
```

Implements the following methods:

| Method | Behavior |
|--------|----------|
| `additional_build_env()` | Adds the package's Perl library directory to `PERL5LIB` for dependent packages during builds.
| `modulefile_prepend_path()` | Adds the package's Perl library directory to `PERL5LIB` in the generated modulefile.
| `build()` | Builds the package using either `Makefile.PL` or `Build.PL` depending on which build system is detected. |
| `install()` | Installs the built Perl module using `make install` or `./Build install`. |

---

#### RPackage

Provides an R package installation flow.

Automatically adds the `r` build and runtime dependency.

Phases:

```text
download → extract → build → install
```

Additional attributes:

| Attribute | Type | Default | Description |
|-----------|------|---------|-------------|
| `cran` | `str \| None` | `None` | CRAN package name used to enable automatic CRAN source URL resolution. |

Implements the following methods:

| Method | Behavior |
|--------|----------|
| `url_for_version(version: str)` | Resolves package source URLs from CRAN when `cran` is set, using the current CRAN release or the CRAN archive for older versions. Falls back to the default URL handling otherwise. |
| `additional_build_env()` | Adds the package's R library directory to `R_LIBS_USER` for dependent packages during builds. |
| `modulefile_prepend_path()` | Adds the package's R library directory to `R_LIBS_USER` in the generated modulefile. |
| `install()` | Runs `R CMD INSTALL --library=<package R library directory> <source directory>`. |

---

#### BinaryPackage

Provides an installation flow for pre-built software archives.

Phases:

```text
download → extract → install
```

Implements the following methods:

| Method | Behavior |
|--------|----------|
| `install()` | Installs the extracted archive contents directly into the package prefix. |

---

### Dependencies

Dependencies are declared using the `Dependency` class through the `depends_on` class attribute. Dependencies are resolved before a package is built or installed, producing resolved package instances with their selected versions and configuration.

```python
from lib.dependency import Dependency

depends_on = [
    Dependency("zlib@1.3.1"),                   # link dependency (default)
    Dependency("cmake@3.30.9", type="build"),   # build-only dependency
    Dependency("python", type="run"),           # runtime dependency
    Dependency("mpi", type=("link", "run")),    # multiple dependency types
]
```

A dependency type can be a single string or a tuple of types when a dependency serves multiple purposes.

| Type | Description |
|------|-------------|
| `link` (default) | The package links against this dependency. Build-system classes determine how link dependencies are exposed during builds, commonly through `apply_toolchain_env()` |
| `build` | Dependency required only while building the package. Its `bin/` directory is added to `PATH` during the build. Build-system classes may provide additional build environment variables through `additional_build_env()`. |
| `run` | Dependency required when using the installed package. Added to the generated modulefile dependencies so it is loaded automatically at runtime. |

Dependency versions can by pinned by including a version in the dependency specification:

```python
Dependency("zlib@1.3.1")
```

If no version is specified, the dependency's default version is used (first entry in its `versions` list).

Resolved dependencies can be accessed using the `dep()` helper:

```python
self.dep("zlib")
```

Packages should not modify resolved dependencies directly. The package manager manages dependency resolution and uses the resolved dependency information throughout the build and installation process.

---

### Generated modulefiles

Installed packages automatically generate modulefiles that configure the user's environment when loaded. Modulefiles can set environment variables, modify search paths, and load other modules.

Runtime dependencies declared with `type="run"` are added to the generated modulefile so they are loaded automatically.

Many common installation paths are automatically added to the modulefile when present.

Packages can customize their generated modulefiles using the `conflicts` and `shell_functions` attributes, along with the `modulefile_prepend_path()` and `modulefile_setenv()` methods described above in the Package class reference.

## Using modulefiles

After installing packages, add the generated modulefile directory to your module search path:

```bash
module use /path/to/modulefiles
```

This adds the directory to `MODULEPATH`, allowing the module system to discover the installed packages.

Packages can then be discovered and loaded:

```bash
module avail
module load package/version
```
