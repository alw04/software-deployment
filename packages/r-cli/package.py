from lib.build_systems.r import RPackage


class RCli(RPackage):
    """Helpers for Developing Command Line Interfaces.

    A suite of tools to build attractive command line interfaces ('CLIs'), from
    semantic elements: headings, lists, alerts, paragraphs, etc.  Supports
    custom themes via a 'CSS'-like language. It also contains a number of lower
    level 'CLI' elements: rules, boxes, trees, and 'Unicode' symbols with
    'ASCII' alternatives. It integrates with the 'crayon' package to support
    'ANSI' terminal colors."""

    homepage = "https://cli.r-lib.org/"
    cran = "cli"

    versions = [
        "3.6.6",
    ]
