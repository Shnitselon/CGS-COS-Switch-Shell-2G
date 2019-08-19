from cloudshell.devices.runners.firmware_runner import FirmwareRunner

from cgs.flows.load_firmware import CgsLoadFirmwareFlow


class CumulusLinuxFirmwareRunner(FirmwareRunner):
    @property
    def load_firmware_flow(self):
        return CgsLoadFirmwareFlow(cli_handler=self.cli_handler, logger=self._logger)
