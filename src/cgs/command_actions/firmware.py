import re

from cloudshell.cli.command_template.command_template_executor import CommandTemplateExecutor

from cgs.command_templates import firmware


class FirmwareActions(object):
    def __init__(self, cli_service, logger):
        """

        :param cli_service:
        :param logger:
        """
        self._cli_service = cli_service
        self._logger = logger

    def set_remote_firmware_file(self, remote_url, action_map=None, error_map=None):
        """

        :param remote_url:
        :param action_map:
        :param error_map:
        :return:
        """
        return CommandTemplateExecutor(cli_service=self._cli_service,
                                       command_template=firmware.SET_REMOTE_FIRMWARE_FILE,
                                       action_map=action_map,
                                       error_map=error_map).execute_command(remote_url=remote_url)

    def set_remote_firmware_user(self, user, action_map=None, error_map=None):
        """

        :param user:
        :param action_map:
        :param error_map:
        :return:
        """
        command_kwargs = {}

        if user:
            command_kwargs.update({"user": user})
            command_template = firmware.SET_REMOTE_FIRMWARE_USER
        else:
            command_template = firmware.SET_REMOTE_FIRMWARE_NO_USER

        return CommandTemplateExecutor(cli_service=self._cli_service,
                                       command_template=command_template,
                                       action_map=action_map,
                                       error_map=error_map).execute_command(**command_kwargs)

    def set_remote_firmware_password(self, password, action_map=None, error_map=None):
        """

        :param password:
        :param action_map:
        :param error_map:
        :return:
        """
        command_kwargs = {}

        if password:
            command_kwargs.update({"password": password})
            command_template = firmware.SET_REMOTE_FIRMWARE_PASSWORD
        else:
            command_template = firmware.SET_REMOTE_FIRMWARE_NO_PASSWORD

        return CommandTemplateExecutor(cli_service=self._cli_service,
                                       command_template=command_template,
                                       action_map=action_map,
                                       error_map=error_map).execute_command(**command_kwargs)

    def start_sw_upgrade(self, action_map=None, error_map=None):
        """

        :param action_map:
        :param error_map:
        :return:
        """
        return CommandTemplateExecutor(cli_service=self._cli_service,
                                       command_template=firmware.START_SW_UPGRADE,
                                       action_map=action_map,
                                       error_map=error_map).execute_command()

    def get_last_error_msg(self, action_map=None, error_map=None):
        """

        :return:
        """
        output = CommandTemplateExecutor(cli_service=self._cli_service,
                                         command_template=firmware.SHOW_SW_UPGRADE_INFO,
                                         action_map=action_map,
                                         error_map=error_map).execute_command()

        sw_details = re.search(r"[Ll]ast\s[Ee]rror\s+[Mm]essage\s+(?P<error_msg>.*)", output)

        if sw_details:
            return sw_details.group("error_msg")

    def get_sw_upgrade_file_status(self, file_name, action_map=None, error_map=None):
        """

        :param file_name:
        :param action_map:
        :param error_map:
        :return:
        """

        output = CommandTemplateExecutor(cli_service=self._cli_service,
                                         command_template=firmware.SHOW_SW_UPGRADE_INFO,
                                         action_map=action_map,
                                         error_map=error_map).execute_command()

        sw_details = re.search(r"[Aa]lternate\s+[Ii]mage\s+(?P<bank>.*)\s+"
                               r"[Ss]oftware\s+[Vv]ersion\s+(?P<sw_version>.*)\s+"
                               r"[Ff]ilename\s+{}\s+".format(file_name) +
                               r"[Ss]tatus\s+(?P<status>.*)\s+", output)

        return sw_details.group("status") if sw_details else ""

    def get_sw_upgrade_file_boot_bank(self, file_name, action_map=None, error_map=None):
        """

        :param file_name:
        :param action_map:
        :param error_map:
        :return:
        """

        output = CommandTemplateExecutor(cli_service=self._cli_service,
                                         command_template=firmware.SHOW_SW_UPGRADE_INFO,
                                         action_map=action_map,
                                         error_map=error_map).execute_command()

        sw_details = re.search(r"[Aa]lternate\s+[Ii]mage\s+(?P<bank>.*)\s+"
                               r"[Ss]oftware\s+[Vv]ersion\s+(?P<sw_version>.*)\s+"
                               r"[Ff]ilename\s+{}\s+".format(file_name) +
                               r"[Ss]tatus\s+(?P<status>.*)\s+", output)

        return sw_details.group("bank")

    def set_remote_firmware_boot_bank(self, boot_bank, action_map=None, error_map=None):
        pass