from collections import OrderedDict

from cloudshell.cli.command_template.command_template import CommandTemplate


SET_REMOTE_FIRMWARE_FILE = CommandTemplate("file-name {remote_url}")

SET_REMOTE_FIRMWARE_USER = CommandTemplate("username {user}")

SET_REMOTE_FIRMWARE_PASSWORD = CommandTemplate("password {password}")

SET_REMOTE_FIRMWARE_NO_USER = CommandTemplate("no username")

SET_REMOTE_FIRMWARE_NO_PASSWORD = CommandTemplate("no password")

START_SW_UPGRADE = CommandTemplate("start")

SHOW_SW_UPGRADE_INFO = CommandTemplate("do show system sw-upgrade")

SET_REMOTE_FIRMWARE_BOOT_BANK = CommandTemplate("boot-bank {boot_bank}")

SYSTEM_REBOOT = CommandTemplate("do system reboot", action_map=OrderedDict(
    [(r"[Rr]eboot.*[yes]", lambda session, logger: session.send_line('yes', logger),)]),)
