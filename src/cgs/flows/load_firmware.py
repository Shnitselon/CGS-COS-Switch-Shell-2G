# from cgs.command_actions.firmware import FirmwareActions
# from cgs.command_actions.system import SystemActions

from cloudshell.devices.flows.cli_action_flows import LoadFirmwareFlow


class CgsLoadFirmwareFlow(LoadFirmwareFlow):
    def execute_flow(self, path, vrf, timeout):
        """

        :param path:
        :param vrf:
        :param timeout:
        :return:
        """
        """
        admin https (webui from 172.16.10.49) on since 2019-08-29 15:06:58 terminal mode
        NPB-I(config)# system sw-upgrade 
        Possible completions:
          boot-bank   The bank the device will boot from on next reboot
          file-name   The file name to download in URI syntax; protocol://path, for example: http://127.0.0.1:80/filename.bin.tar
          password    The password to be used when accessing the download server
          start       Start software upgrade now
          stop        Stop software upgrade now
          username    The username to be used when accessing the download server

        """
        # with self._cli_handler.get_cli_service(self._cli_handler.root_mode) as cli_service:
        #     system_actions = SystemActions(cli_service=cli_service, logger=self._logger)
        #     firmware_actions = FirmwareActions(cli_service=cli_service, logger=self._logger)
        #
        #     self._logger.info("Loading firmware: {}".format(path))
        #     output = firmware_actions.load_firmware(image_path=path, timeout=timeout)
        #
        #     try:
        #         self._logger.info("Rebooting device...")
        #         output += system_actions.reboot()
        #     except Exception:
        #         self._logger.debug("Reboot session exception:", exc_info=True)
        #
        #     self._logger.info("Reconnecting session...")
        #     cli_service.reconnect(timeout)
        #     return output