from cloudshell.cli.command_mode_helper import CommandModeHelper
from cloudshell.devices.cli_handler_impl import CliHandlerImpl

from cgs.cli.command_modes import EnableCommandMode
from cgs.cli.command_modes import ConfigCommandMode


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
