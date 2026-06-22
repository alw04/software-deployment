from lib.build_systems.autotools import AutotoolsPackage


class Openldap(AutotoolsPackage):
    """
    OpenLDAP Software is an open source implementation of the Lightweight
    Directory Access Protocol. The suite includes:

    slapd - stand-alone LDAP daemon (server)
    libraries implementing the LDAP protocol, and
    utilities, tools, and sample clients.
    """

    homepage = "https://www.openldap.org/"
    url = "https://www.openldap.org/software/download/OpenLDAP/openldap-release/openldap-{version}.tgz"

    versions = [
        "2.6.8",
    ]
