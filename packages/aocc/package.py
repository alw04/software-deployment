from lib.build_systems.binary import BinaryPackage


class Aocc(BinaryPackage):
    """
    The AOCC compiler system is a high performance, production quality code
    generation tool.  The AOCC environment provides various options to developers
    when building and optimizing C, C++, and Fortran applications targeting 32-bit
    and 64-bit Linux platforms.  The AOCC compiler system offers a high level of
    advanced optimizations, multi-threading and processor support that includes
    global optimization, vectorization, inter-procedural analyses, loop
    transformations, and code generation.  AMD also provides highly optimized
    libraries, which extract the optimal performance from each x86 processor core
    when utilized.  The AOCC Compiler Suite simplifies and accelerates development
    and tuning for x86 applications.
    """

    homepage = "https://www.amd.com/en/developer/aocc.html"

    def url_for_version(self, version):
        major_minor = ".".join(version.split(".")[:2]).replace(".", "-")
        return f"https://download.amd.com/developer/eula/aocc/aocc-{major_minor}/aocc-compiler-{version}.tar"

    versions = [
        "5.0.0",
    ]
