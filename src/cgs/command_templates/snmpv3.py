from cloudshell.cli.command_template.command_template import CommandTemplate


ENABLE_SNMP = CommandTemplate("v3 true")

SET_DEFAULT_AUTH_AND_PRIV = CommandTemplate("auth-access read-only auth-protocol none priv-protocol none")

ADD_SNMP_USER_AUTH = CommandTemplate("auth-protocol {snmp_auth_proto} auth-pass {snmp_password}")

ADD_SNMP_USER_PRIV = CommandTemplate("priv-protocol {snmp_priv_proto} priv-pass {snmp_priv_key}")

REMOVE_SNMP_USER = CommandTemplate("no v3-username {snmp_user}")

DISABLE_SNMP = CommandTemplate("v3 false")
