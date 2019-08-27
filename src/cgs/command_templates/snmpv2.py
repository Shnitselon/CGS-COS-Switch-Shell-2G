from cloudshell.cli.command_template.command_template import CommandTemplate


SHOW_SNMP_STATUS = CommandTemplate("show system snmp")

ENABLE_SNMP = CommandTemplate("system snmp v2c true")

SET_READ_COMMUNITY = CommandTemplate("system snmp read-community {snmp_community}")

SET_WRITE_COMMUNITY = CommandTemplate("system snmp write-community {snmp_community}")

DISABLE_SNMP = CommandTemplate("system snmp v2c false")

UNSET_READ_COMMUNITY = CommandTemplate("no system snmp read-community {snmp_community}")

UNSET_WRITE_COMMUNITY = CommandTemplate("no system snmp write-community {snmp_community}")
