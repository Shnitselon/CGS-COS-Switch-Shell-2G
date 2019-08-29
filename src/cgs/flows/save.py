from cgs.command_actions.system import SystemActions

from cloudshell.devices.flows.cli_action_flows import SaveConfigurationFlow
from cloudshell.devices.networking_utils import UrlParser


class CgsSaveFlow(SaveConfigurationFlow):
    def execute_flow(self, folder_path, configuration_type, vrf_management_name=None):
        """

        :param folder_path:
        :param configuration_type:
        :param vrf_management_name:
        :return:
        """
        url = UrlParser.parse_url(folder_path)
        config_file = url.get(UrlParser.FILENAME)

        with self._cli_handler.get_cli_service(self._cli_handler.config_mode) as config_session:
            system_actions = SystemActions(cli_service=config_session, logger=self._logger)
            system_actions.save_config_file(config_file=config_file)

            if "://" in folder_path:
                with config_session.enter_mode(self._cli_handler.enable_mode):
                    system_actions.export_config_file(config_file=config_file,
                                                      remote_url=folder_path,
                                                      user=url.get(UrlParser.USERNAME),
                                                      password=url.get(UrlParser.PASSWORD))

                    system_actions.delete_config_file(config_file=config_file)
