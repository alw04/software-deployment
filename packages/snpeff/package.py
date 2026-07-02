from lib.dependency import Dependency
from lib.package import Package


class Snpeff(Package):
    """SnpEff is a variant annotation and effect prediction tool. It
    annotates and predicts the effects of genetic variants (such as
    amino acid changes)."""

    homepage = "https://pcingola.github.io/SnpEff/"
    url = "https://snpeff-public.s3.amazonaws.com/versions/snpEff_v{version}_core.zip"

    versions = [
        "5_4c",
        "5_1d",
    ]

    depends_on = [
        Dependency("openjdk", type="run"),
    ]

    def install(self):
        for file in ["snpEff.jar", "SnpSift.jar", "snpEff.config"]:
            self.install_file(self.build_dir / file, self.prefix / file)

        for script in ["snpEff", "snpSift"]:
            self.install_binary(self.build_dir / "scripts" / script)
