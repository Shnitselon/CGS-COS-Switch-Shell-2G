from collections import OrderedDict

from cloudshell.cli.command_template.command_template import CommandTemplate


ERROR_MAP = OrderedDict([("[Ee]rror:", "An error occurred while executing a CLI command")])

EXPORT_CONFIG_FILE_ANONYMOUS = CommandTemplate(
    "system config-files export local-file {config_file} remote-url {remote_url}",
    action_map=OrderedDict([(r"[Ee]rror:.*[Aa]access [Dd]enied", "Failed uploading file: Access denied")]),
    error_map=ERROR_MAP)

EXPORT_CONFIG_FILE = CommandTemplate(
    "system config-files export local-file {config_file} remote-url {remote_url} username {user} password {password}",
    action_map=OrderedDict([(r"[Ee]rror:.*[Aa]access [Dd]enied", "Failed uploading file: Access denied")]),
    error_map=ERROR_MAP)

IMPORT_CONFIG_FILE_ANONYMOUS = CommandTemplate(
    "system config-files import local-file {config_file} remote-url {remote_url}",
    error_map=ERROR_MAP,
    action_map=OrderedDict([
        (r"[Aa]lready [Ee]xists.*[Oo]verride.*[Yy]/[Nn]",
         lambda session, logger: session.send_line('y', logger))]))

IMPORT_CONFIG_FILE = CommandTemplate(
    "system config-files import local-file {config_file} remote-url {remote_url} username {user} password {password}",
    error_map=ERROR_MAP,
    action_map=OrderedDict([
        (r"[Aa]lready [Ee]xists.*[Oo]verride.*[Yy]/[Nn]",
         lambda session, logger: session.send_line('y', logger))]))

SAVE_LOCAL_CONFIG_FILE = CommandTemplate(
    "system config-files save local-file {config_file}",
    action_map=OrderedDict([
        (r"[Aa]lready [Ee]xists.*[Oo]verwrite?.*([Yy]/[Nn])",
         lambda session, logger: session.send_line('y', logger),)]),
    error_map=ERROR_MAP)

LOAD_LOCAL_CONFIG_FILE = CommandTemplate(
    "system config-files load local-file {config_file}",
    action_map=OrderedDict([
        (r"[Aa]lready [Ee]xists.*[Oo]verride.*[Yy]/[Nn]",
         lambda session, logger: session.send_line('y', logger),)]),
    error_map=ERROR_MAP)

DELETE_LOCAL_CONFIG_FILE = CommandTemplate("system config-files delete local-file {config_file}", error_map=ERROR_MAP)
