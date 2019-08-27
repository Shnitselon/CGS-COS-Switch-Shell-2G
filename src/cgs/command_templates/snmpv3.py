from cloudshell.cli.command_template.command_template import CommandTemplate


ENABLE_SNMP = CommandTemplate("system snmp v3 true")

ADD_SNMP_USER = CommandTemplate("system snmp v3-username {snmp_user} auth-access read-only auth-protocol none "
                                "priv-protocol none")

ADD_SNMP_USER_AUTH = CommandTemplate("system snmp v3-username {snmp_user} auth-protocol {snmp_auth_proto} "
                                     "auth-pass {snmp_password}")

ADD_SNMP_USER_PRIV = CommandTemplate("system snmp v3-username {snmp_user} priv-protocol {snmp_priv_proto} "
                                     "priv-pass {snmp_priv_key}")

REMOVE_SNMP_USER = CommandTemplate("no system snmp v3-username {snmp_user}")

DISABLE_SNMP = CommandTemplate("system snmp v3 false")
