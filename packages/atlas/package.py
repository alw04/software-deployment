from lib.build_systems.autotools import AutotoolsPackage
from lib.dependency import Dependency


class Atlas(AutotoolsPackage):  # Not Autotools, but follows a similar workflow
    """Automatically Tuned Linear Algebra Software, generic shared ATLAS is an
    approach for the automatic generation and optimization of numerical
    software. Currently ATLAS supplies optimized versions for the complete set
    of linear algebra kernels known as the Basic Linear Algebra Subroutines
    (BLAS), and a subset of the linear algebra routines in the LAPACK library.
    """

    homepage = "https://math-atlas.sourceforge.net/"
    url = "https://sourceforge.net/projects/math-atlas/files/Stable/{version}/atlas{version}.tar.bz2"

    versions = [
        "3.10.3",
    ]

    depends_on = [
        Dependency("openblas"),
    ]

    max_jobs = 1

    source_subdir = "build"

    def configure(self):
        self.build_dir.mkdir(parents=True, exist_ok=True)
        self.run_cmd(
            [
                str(self.build_path / "configure"),
                f"--prefix={self.prefix}",
                "--cripple-atlas-performance",
            ],
            cwd=self.build_dir,
        )
