from cloudshell.cli.command_mode_helper import CommandModeHelper
from cloudshell.devices.cli_handler_impl import CliHandlerImpl

from cgs.cli.command_modes import EnableCommandMode
from cgs.cli.command_modes import ConfigCommandMode
from cgs.cli.command_modes import SNMPConfigCommandMode
from cgs.cli.command_modes import SwUpgradeConfigCommandMode


class CgsCliHandler(CliHandlerImpl):
    def __init__(self, cli, resource_config, logger, api):
        super(CgsCliHandler, self).__init__(cli, resource_config, logger, api)
        self.modes = CommandModeHelper.create_command_mode(resource_config, api)

    @property
    def enable_mode(self):
        """

        :rtype: EnableCommandMode
        """
        return self.modes[EnableCommandMode]

    @property
    def config_mode(self):
        """

        :rtype: ConfigCommandMode
        """
        return self.modes[ConfigCommandMode]

    @property
    def snmp_config_mode(self):
        """

        :rtype: SNMPConfigCommandMode
        """
        return self.modes[SNMPConfigCommandMode]

    @property
    def sw_upgrade_config_mode(self):
        """

        :rtype: SNMPConfigCommandMode
        """
        return self.modes[SwUpgradeConfigCommandMode]

    def on_session_start(self, session, logger):
        """Perform some default commands when session just opened (like 'no logging console')

        :param session:
        :param logger:
        :return:
        """
        session.send_line("config", logger)
        session.send_line("system cli session paginate false", logger)
        session.send_line("commit", logger)
