from lib.build_systems.cmake import CMakePackage
from lib.dependency import Dependency


class Geant4(CMakePackage):
    """Geant4 is a toolkit for the simulation of the passage of particles
    through matter. Its areas of application include high energy, nuclear
    and accelerator physics, as well as studies in medical and space
    science."""

    homepage = "http://geant4.cern.ch/"
    url = "https://gitlab.cern.ch/geant4/geant4/-/archive/v{version}/geant4-v{version}.tar.gz"

    versions = [
        "11.3.2",
    ]

    depends_on = [
        Dependency("expat"),
    ]
