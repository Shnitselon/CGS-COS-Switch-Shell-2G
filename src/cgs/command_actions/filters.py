from cloudshell.cli.command_template.command_template_executor import CommandTemplateExecutor

from cgs.command_templates import filters
from cgs.helpers.filters import Filters


class FiltersActions(object):
    def __init__(self, cli_service, logger):
        """

        :param cli_service: default mode cli_service
        :type cli_service: CliService
        :param logger:
        :type logger: Logger
        :return:
        """
        self._cli_service = cli_service
        self._logger = logger

    def get_filters(self):
        """

        :rtype: Filters
        """
        connections = CommandTemplateExecutor(cli_service=self._cli_service,
                                              command_template=filters.SHOW_FILTERS,
                                              remove_prompt=True).execute_command()

        return Filters(self._logger, connections)

    def remove_filter(self, filter_id, action_map=None, error_map=None):
        """

        :param filter_id:
        :param action_map:
        :param error_map:
        :return:
        """
        return CommandTemplateExecutor(cli_service=self._cli_service,
                                       command_template=filters.REMOVE_FILTER,
                                       action_map=action_map,
                                       error_map=error_map).execute_command(filter_id=filter_id)

    def remove_filters(self, filter_ids, action_map=None, error_map=None):
        """Remove filters

        It's important to delete all needed filters in one command.
        After deleting a filter next filters change their ids
        :param list[str] filter_ids:
        :param action_map:
        :param error_map:
        :return:
        """
        if len(filter_ids) > 1:
            return CommandTemplateExecutor(
                cli_service=self._cli_service,
                action_map=action_map,
                error_map=action_map,
                command_template=filters.REMOVE_FILTERS).execute_command(filter_ids=",".join(filter_ids))

        elif len(filter_ids) == 1:
            return self.remove_filter(filter_id=filter_ids[0], action_map=action_map, error_map=error_map)
