from lib.build_systems.autotools import AutotoolsPackage


class Gawk(AutotoolsPackage):
    """If you are like many computer users, you would frequently like to make
    changes in various text files wherever certain patterns appear, or
    extract data from parts of certain lines while discarding the
    rest. To write a program to do this in a language such as C or
    Pascal is a time-consuming inconvenience that may take many lines
    of code. The job is easy with awk, especially the GNU
    implementation: gawk.

    The awk utility interprets a special-purpose programming language
    that makes it possible to handle simple data-reformatting jobs
    with just a few lines of code.
    """

    homepage = "https://www.gnu.org/software/gawk/"
    url = "https://ftp.gnu.org/gnu/gawk/gawk-{version}.tar.xz"

    versions = [
        "5.3.1",
    ]
