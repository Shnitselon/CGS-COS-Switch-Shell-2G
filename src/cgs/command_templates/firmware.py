from collections import OrderedDict

from cloudshell.cli.command_template.command_template import CommandTemplate


SET_REMOTE_FIRMWARE_FILE = CommandTemplate("system sw-upgrade file-name {remote_url}")

SET_REMOTE_FIRMWARE_USER = CommandTemplate("system sw-upgrade username {user}")

SET_REMOTE_FIRMWARE_PASSWORD = CommandTemplate("system sw-upgrade password {password}")

SET_REMOTE_FIRMWARE_NO_USER = CommandTemplate("no username")

SET_REMOTE_FIRMWARE_NO_PASSWORD = CommandTemplate("no password")

START_SW_UPGRADE = CommandTemplate("system sw-upgrade start")

SHOW_SW_UPGRADE_INFO = CommandTemplate("do show system sw-upgrade")

SET_REMOTE_FIRMWARE_BOOT_BANK = CommandTemplate("system sw-upgrade boot-bank {boot_bank}")

SYSTEM_REBOOT = CommandTemplate("do system reboot", action_map=OrderedDict(
    [(r"[Rr]eboot.*[yes]", lambda session, logger: session.send_line('yes', logger),)]),)
