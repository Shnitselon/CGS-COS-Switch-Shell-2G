import re

from cloudshell.cli.session.session_exceptions import CommandExecutionException
from cloudshell.devices.flows.cli_action_flows import LoadFirmwareFlow
from cloudshell.devices.networking_utils import UrlParser

from cgs.command_actions.firmware import FirmwareActions
from cgs.command_actions.commit import CommitActions


class CgsLoadFirmwareFlow(LoadFirmwareFlow):
    def execute_flow(self, path, vrf, timeout):
        """

        :param path:
        :param vrf:
        :param timeout:
        :return:
        """
        url = UrlParser.parse_url(path)

        """
        NPB-I# show system sw-upgrade 
        Software
        =============================================
        Next System Boot            Bank A 
        
        Running Image               Bank A
        Software Version            2.6.0
        Filename                    NPB-I-x86-2.6.0.bin.tar
        
        Alternate Image             Bank B
        Software Version            2.6.1
        Filename                    NPB-II-x86-2.6.1.bin.tar
        Status                      Corrupted
        
        Last Error Message          Failed burn image to disk
        
        User                        cgs
        Password                    
        File                        ftp://cgs@192.168.201.100/NPB-II-x86-2.6.1.bin.tar
        NPB-I# 
        
        """

        with self._cli_handler.get_cli_service(self._cli_handler.config_mode) as config_session:
            commit_actions = CommitActions(cli_service=config_session, logger=self._logger)
            firmware_actions = FirmwareActions(cli_service=config_session, logger=self._logger)

            try:
                firmware_actions.set_remote_firmware_file(remote_url=path)
                firmware_actions.set_remote_firmware_user(user=url.get(UrlParser.USERNAME))
                firmware_actions.set_remote_firmware_password(password=url.get(UrlParser.PASSWORD))
                commit_actions.commit()

            except CommandExecutionException:
                self._logger.exception("Failed to set remote firmware file:")
                commit_actions.abort()
                raise

            firmware_actions.start_sw_upgrade()
            sw_info = firmware_actions.show_sw_upgrade_info()

            sw_info_status = re.search(r"[Ss]tatus\s+(?P<status>.*)\n", sw_info).group("status")

            # todo: find correct bank block first !!!

            sw_details = re.search(r"[Aa]lternate\s+[Ii]mage\s+(?P<bank>.*)\n.*"
                                   r"[Ff]ilename\s+NPB-II-x86-2.6.1.bin.tar\n"
                                   r"[Ss]tatus\s+(?P<status>.*)\n.*",
                                   sw_info)

            import ipdb;ipdb.set_trace()
            pass