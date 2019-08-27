from cloudshell.cli.command_template.command_template import CommandTemplate


ENABLE_SNMP = CommandTemplate("system snmp v3 true")

# todo: fix this when no priv-pass or auth-pass !!!!
ADD_SNMP_USER = CommandTemplate("system snmp v3-username {snmp_user} auth-access read-only auth-protocol {snmp_auth_proto} auth-pass {snmp_password} priv-protocol {snmp_priv_proto} priv-pass {snmp_priv_key}")

REMOVE_SNMP_USER = CommandTemplate("no system snmp v3-username {snmp_user}")

DISABLE_SNMP = CommandTemplate("system snmp v3 false")
