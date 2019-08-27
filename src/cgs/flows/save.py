# from cgs.command_actions.system import SystemActions

from cloudshell.devices.flows.cli_action_flows import SaveConfigurationFlow


class CgsSaveFlow(SaveConfigurationFlow):
    def execute_flow(self, folder_path, configuration_type, vrf_management_name=None):
        """

        :param folder_path:
        :param configuration_type:
        :param vrf_management_name:
        :return:
        """
        with self._cli_handler.get_cli_service(self._cli_handler.enable_mode) as enable_session:
            # system_actions = SystemActions(cli_service=enable_session, logger=self._logger)
            "system config-files export local-file Test remote-url ftp://test_user:test_password@192.168.42.102/CGS_COS_Switch_Shell_2G-running-270819-173934"

            """
            Error: Couldn't export: Failed uploading file: Server denied you to change to the given directory
            NPB-I# system config-files export local-file Test remote-url ftp://ftp.dlptest.com/CGS_COS_Switch_Shell_2G-running-270819-173934 password fLDScD4Ynth0p4OJ6bW6qCxjh user dlpuser@dlptest.com       
            Uploading...
            Success.
  
            NPB-I# system config-files export local-file Test remote-url ftp://ftp.dlptest.com/upload/CGS_COS_Switch_Shell_2G-running-270819-173934  
            Uploading...
            Fail!
            Error: Couldn't export: Failed uploading file: Access denied: 530

            NPB-I# system config-files export local-file Test remote-url ftp://dlpuser@dlptest.com:fLDScD4Ynth0p4OJ6bW6qCxjh@ftp.dlptest.com/upload/CGS_COS_Switch_Shell_2G-running-270819-173934
            Uploading...
            Fail!
            Error: Couldn't export: Failed uploading file: Access denied: 530

            """
            #

            # self._logger.info("Creating backup files...")
            # backup_dir = system_actions.create_tmp_dir()
            #
            # for conf_folder in self.CONF_FOLDERS:
            #     system_actions.copy_folder(src_folder=conf_folder, dst_folder=backup_dir)
            #
            # for conf_file in self.CONF_FILES:
            #     system_actions.copy_file(src_file=conf_file, dst_folder=backup_dir)
            #
            # self._logger.info("Compressing backup directory '{}' to .tar archive...".format(backup_dir))
            # backup_file = system_actions.create_tmp_file()
            # system_actions.tar_compress_folder(compress_name=backup_file, folder=backup_dir)
            #
            # self._logger.info("Uploading backup .tar archive '{}' via curl".format(backup_file))
            # system_actions.curl_upload_file(file_path=backup_file, remote_url=folder_path)