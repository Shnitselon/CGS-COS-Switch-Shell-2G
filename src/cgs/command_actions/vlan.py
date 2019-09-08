from cloudshell.cli.command_template.command_template_executor import CommandTemplateExecutor

from cgs.command_actions.filters import FiltersActions
from cgs.command_templates import vlan as vlan_tmpl


class VlanActions(FiltersActions):

    VLAN_FILTER_NAME_TPL = "vlan-{}"
    TRUNK_VLAN_CLASSIFIER = "l2"
    ACCESS_VLAN_PACKET_PROCESSING = "vlan-outer"

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

    def add_access_vlan_filter(self, vlan, port, action_map=None, error_map=None):
        """

        :param vlan:
        :param port:
        :param action_map:
        :param error_map:
        :return:
        """
        return CommandTemplateExecutor(
            cli_service=self._cli_service,
            command_template=vlan_tmpl.ADD_ACCESS_VLAN_FILTER,
            action_map=action_map,
            error_map=error_map).execute_command(name=self.VLAN_FILTER_NAME_TPL.format(vlan),
                                                 vlan=vlan,
                                                 port=port)

    def add_trunk_vlan_filter(self, vlan_range, port, action_map=None, error_map=None):
        """

        :param vlan_range:
        :param port:
        :param action_map:
        :param error_map:
        :return:
        """
        return CommandTemplateExecutor(
            cli_service=self._cli_service,
            command_template=vlan_tmpl.ADD_TRUNK_VLAN_FILTER,
            action_map=action_map,
            error_map=error_map).execute_command(name=self.VLAN_FILTER_NAME_TPL.format(vlan_range),
                                                 vlan_range=vlan_range,
                                                 port=port)

    def get_access_vlan_filters_id(self, vlan, port, action_map=None, error_map=None):
        """

        :param vlan:
        :param port:
        :param action_map:
        :param error_map:
        :return:
        """
        return self.get_filters(action_map=action_map, error_map=error_map).find_filters_by_fields(
            name=self.VLAN_FILTER_NAME_TPL.format(vlan),
            input_port=port,
            classifiers="",
            packet_processing=self.ACCESS_VLAN_PACKET_PROCESSING)

    def get_trunk_vlan_filters_id(self, vlan_range, port, action_map=None, error_map=None):
        """

        :param vlan_range:
        :param port:
        :param action_map:
        :param error_map:
        :return:
        """
        return self.get_filters(action_map=action_map, error_map=error_map).find_filters_by_fields(
            name=self.VLAN_FILTER_NAME_TPL.format(vlan_range),
            input_port=port,
            classifiers=self.TRUNK_VLAN_CLASSIFIER,
            packet_processing="")
