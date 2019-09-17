from cloudshell.cli.command_template.command_template import CommandTemplate


SHOW_FILTERS = CommandTemplate("do show filters filter")

REMOVE_FILTER = CommandTemplate("filters delete filter {filter_id}")
