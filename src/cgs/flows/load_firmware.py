from datetime import datetime
from datetime import timedelta
import time

from cloudshell.cli.session.session_exceptions import CommandExecutionException
from cloudshell.devices.flows.cli_action_flows import LoadFirmwareFlow
from cloudshell.devices.networking_utils import UrlParser

from cgs.command_actions.firmware import FirmwareActions
from cgs.command_actions.commit import CommitActions


class CgsLoadFirmwareFlow(LoadFirmwareFlow):
    IMAGE_VALIDATION_WAITING_TIMEOUT = 5 * 60
    IMAGE_VALIDATION_WAITING_INTERVAL = 5
    IMAGE_VALIDATION_SUCCESS_STATE = "Valid"

    @staticmethod
    def _convert_boot_bank(boot_bank):
        """

        :param boot_bank:
        :return:
        """
        return boot_bank.lower().replace(" ", "-")

    @staticmethod
    def _get_firmware_file_name(path):
        """

        :param path:
        :return:
        """
        return path.split("/")[-1]

    def execute_flow(self, path, vrf, timeout):
        """

        :param path:
        :param vrf:
        :param timeout:
        :return:
        """
        url = UrlParser.parse_url(path)
        file_name = self._get_firmware_file_name(path)

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
            self._wait_for_image_validation(firmware_actions, file_name)
            boot_bank = firmware_actions.get_sw_upgrade_file_boot_bank(file_name=file_name)
            boot_bank = self._convert_boot_bank(boot_bank=boot_bank)

            try:
                firmware_actions.set_remote_firmware_boot_bank(boot_bank=boot_bank)
                commit_actions.commit()

            except CommandExecutionException:
                self._logger.exception("Failed to set remote firmware file boot bank:")
                commit_actions.abort()
                raise

            try:
                self._logger.info("Rebooting device...")
                firmware_actions.system_reboot()
            except Exception:
                self._logger.debug("Reboot session exception:", exc_info=True)

            self._logger.info("Reconnecting session...")
            config_session.reconnect(timeout)

    def _wait_for_image_validation(self, firmware_actions, file_name):
        """

        :param firmware_actions:
        :param file_name:
        :return:
        """
        timeout_time = datetime.now() + timedelta(seconds=self.IMAGE_VALIDATION_WAITING_TIMEOUT)
        status = ""

        while status.lower() != self.IMAGE_VALIDATION_SUCCESS_STATE.lower():
            error_msg = firmware_actions.get_last_error_msg()

            if error_msg:
                raise Exception("Unable to validate firmware file. {}".format(error_msg))

            status = firmware_actions.get_sw_upgrade_file_status(file_name=file_name)

            self._logger.info("Firmawe image status is '{}'. Waiting...".format(status))
            time.sleep(self.IMAGE_VALIDATION_WAITING_INTERVAL)

            if datetime.now() > timeout_time:
                raise Exception("Unable to check firmware file state")
