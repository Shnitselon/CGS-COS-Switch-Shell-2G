from cloudshell.cli.command_template.command_template import CommandTemplate


ADD_ACCESS_VLAN_FILTER = CommandTemplate("filters add name {name} vlan-set-outer {vlan} "
                                         "input-ports {port} action redirect output-ports all")

ADD_TRUNK_VLAN_FILTER = CommandTemplate("filters add name {name} l2-vlan {vlan_range} "
                                        "input-ports {port} action redirect output-ports all")
