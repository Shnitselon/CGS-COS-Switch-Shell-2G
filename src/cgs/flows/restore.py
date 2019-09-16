from cgs.command_actions.save_restore import SaveRestoreActions

from cloudshell.devices.flows.cli_action_flows import RestoreConfigurationFlow
from cloudshell.devices.networking_utils import UrlParser


class CgsRestoreFlow(RestoreConfigurationFlow):
    def execute_flow(self, path, configuration_type, restore_method, vrf_management_name=None):
        """

        :param path:
        :param configuration_type:
        :param restore_method:
        :param vrf_management_name:
        :return:
        """
        url = UrlParser.parse_url(path)
        config_file = url.get(UrlParser.FILENAME)

        with self._cli_handler.get_cli_service(self._cli_handler.config_mode) as config_session:
            restore_actions = SaveRestoreActions(cli_service=config_session, logger=self._logger)
            if "://" in path:
                with config_session.enter_mode(self._cli_handler.enable_mode):
                    restore_actions.import_config_file(config_file=config_file,
                                                       remote_url=path,
                                                       user=url.get(UrlParser.USERNAME),
                                                       password=url.get(UrlParser.PASSWORD))

            restore_actions.load_config_file(config_file=config_file)
