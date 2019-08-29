from cloudshell.cli.command_template.command_template import CommandTemplate


ABORT = CommandTemplate("abort")
COMMIT = CommandTemplate("commit", error_map={"[Aa]borted:": "Unable to commit changes"})
