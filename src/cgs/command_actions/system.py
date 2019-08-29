from cloudshell.cli.command_template.command_template_executor import CommandTemplateExecutor

from cgs.command_templates import system


class SystemActions(object):
    def __init__(self, cli_service, logger):
        """

        :param cli_service:
        :param logger:
        """
        self._cli_service = cli_service
        self._logger = logger

    def save_config_file(self, config_file, action_map=None, error_map=None):
        """

        :param config_file:
        :param action_map:
        :param error_map:
        :return:
        """
        return CommandTemplateExecutor(cli_service=self._cli_service,
                                       command_template=system.SAVE_LOCAL_CONFIG_FILE,
                                       action_map=action_map,
                                       error_map=error_map).execute_command(config_file=config_file)

    def load_config_file(self, config_file, action_map=None, error_map=None):
        """

        :param config_file:
        :param action_map:
        :param error_map:
        :return:
        """
        return CommandTemplateExecutor(cli_service=self._cli_service,
                                       command_template=system.LOAD_LOCAL_CONFIG_FILE,
                                       action_map=action_map,
                                       error_map=error_map).execute_command(config_file=config_file)

    def export_config_file(self, config_file, remote_url, user, password, action_map=None, error_map=None):
        """

        :param config_file:
        :param remote_url:
        :param user:
        :param password:
        :param action_map:
        :param error_map:
        :return:
        """
        command_kwargs = {"config_file": config_file, "remote_url": remote_url}

        if user:
            command_kwargs.update({"user": user, "password": password})
            command_template = system.EXPORT_CONFIG_FILE
        else:
            command_template = system.EXPORT_CONFIG_FILE_ANONYMOUS

        return CommandTemplateExecutor(cli_service=self._cli_service,
                                       command_template=command_template,
                                       action_map=action_map,
                                       error_map=error_map).execute_command(**command_kwargs)

    def import_config_file(self, config_file, remote_url, user, password, action_map=None, error_map=None):
        """

        :param config_file:
        :param remote_url:
        :param user:
        :param password:
        :param action_map:
        :param error_map:
        :return:
        """
        command_kwargs = {"config_file": config_file, "remote_url": remote_url}

        if user:
            command_kwargs.update({"user": user, "password": password})
            command_template = system.IMPORT_CONFIG_FILE
        else:
            command_template = system.IMPORT_CONFIG_FILE_ANONYMOUS

        return CommandTemplateExecutor(cli_service=self._cli_service,
                                       command_template=command_template,
                                       action_map=action_map,
                                       error_map=error_map).execute_command(**command_kwargs)

    def delete_config_file(self, config_file, action_map=None, error_map=None):
        """

        :param config_file:
        :param action_map:
        :param error_map:
        :return:
        """
        return CommandTemplateExecutor(cli_service=self._cli_service,
                                       command_template=system.DELETE_LOCAL_CONFIG_FILE,
                                       action_map=action_map,
                                       error_map=error_map).execute_command(config_file=config_file)
