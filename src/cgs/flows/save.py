# from cloudshell.cumulus.linux.command_actions.system import SystemActions
from cloudshell.devices.flows.cli_action_flows import SaveConfigurationFlow


class CgsSaveFlow(SaveConfigurationFlow):
    def execute_flow(self, folder_path, configuration_type, vrf_management_name=None):
        """

        :param folder_path:
        :param configuration_type:
        :param vrf_management_name:
        :return:
        """
        pass
        # with self._cli_handler.get_cli_service(self._cli_handler.root_mode) as cli_service:
        #     system_actions = SystemActions(cli_service=cli_service, logger=self._logger)
        #
        #     self._logger.info("Creating backup files...")
        #     backup_dir = system_actions.create_tmp_dir()
        #
        #     for conf_folder in self.CONF_FOLDERS:
        #         system_actions.copy_folder(src_folder=conf_folder, dst_folder=backup_dir)
        #
        #     for conf_file in self.CONF_FILES:
        #         system_actions.copy_file(src_file=conf_file, dst_folder=backup_dir)
        #
        #     self._logger.info("Compressing backup directory '{}' to .tar archive...".format(backup_dir))
        #     backup_file = system_actions.create_tmp_file()
        #     system_actions.tar_compress_folder(compress_name=backup_file, folder=backup_dir)
        #
        #     self._logger.info("Uploading backup .tar archive '{}' via curl".format(backup_file))
        #     system_actions.curl_upload_file(file_path=backup_file, remote_url=folder_path)