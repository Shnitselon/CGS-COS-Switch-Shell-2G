from cloudshell.devices.runners.configuration_runner import ConfigurationRunner

from cgs.flows.restore import CgsRestoreFlow
from cgs.flows.save import CgsSaveFlow


class CgsConfigurationRunner(ConfigurationRunner):
    @property
    def restore_flow(self):
        return CgsRestoreFlow(cli_handler=self.cli_handler, logger=self._logger)

    @property
    def save_flow(self):
        return CgsSaveFlow(cli_handler=self.cli_handler, logger=self._logger)

    @property
    def file_system(self):
        return "flash:"
