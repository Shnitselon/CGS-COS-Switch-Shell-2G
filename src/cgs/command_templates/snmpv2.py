from cloudshell.cli.command_template.command_template import CommandTemplate


ENABLE_SNMP = CommandTemplate("v2c true")

SET_READ_COMMUNITY = CommandTemplate("read-community {snmp_community}")

SET_WRITE_COMMUNITY = CommandTemplate("write-community {snmp_community}")

DISABLE_SNMP = CommandTemplate("v2c false")

UNSET_READ_COMMUNITY = CommandTemplate("no read-community {snmp_community}")

UNSET_WRITE_COMMUNITY = CommandTemplate("no write-community {snmp_community}")
