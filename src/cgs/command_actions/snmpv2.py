import re

from cloudshell.cli.command_template.command_template_executor import CommandTemplateExecutor

from cgs.command_templates import snmpv2


class SnmpV2Actions(object):
    def __init__(self, cli_service, logger):
        """

        :param cli_service:
        :param logger:
        """
        self._cli_service = cli_service
        self._logger = logger

    # todo: rework !!!
    def is_snmp_running(self, action_map=None, error_map=None):
        """

        :return:
        """
        snmp_status = CommandTemplateExecutor(cli_service=self._cli_service,
                                              command_template=snmpv2.SHOW_SNMP_STATUS,
                                              action_map=action_map,
                                              error_map=error_map).execute_command()

        return True
        # return bool(re.search(r"current[\s]+status[\s]+active", snmp_status, flags=re.IGNORECASE | re.MULTILINE))

    def enable_snmp(self, action_map=None, error_map=None):
        """

        :param action_map:
        :param error_map:
        :return:
        """
        return CommandTemplateExecutor(cli_service=self._cli_service,
                                       command_template=snmpv2.ENABLE_SNMP,
                                       action_map=action_map,
                                       error_map=error_map).execute_command()

    def set_read_community(self, snmp_community, action_map=None, error_map=None):
        """

        :param snmp_community:
        :param action_map:
        :param error_map:
        :return:
        """
        return CommandTemplateExecutor(cli_service=self._cli_service,
                                       command_template=snmpv2.SET_READ_COMMUNITY,
                                       action_map=action_map,
                                       error_map=error_map).execute_command(snmp_community=snmp_community)

    def set_write_community(self, snmp_community, action_map=None, error_map=None):
        """

        :param snmp_community:
        :param action_map:
        :param error_map:
        :return:
        """
        return CommandTemplateExecutor(cli_service=self._cli_service,
                                       command_template=snmpv2.SET_WRITE_COMMUNITY,
                                       action_map=action_map,
                                       error_map=error_map).execute_command(snmp_community=snmp_community)

    def disable_snmp(self, action_map=None, error_map=None):
        """

        :param action_map:
        :param error_map:
        :return:
        """
        return CommandTemplateExecutor(cli_service=self._cli_service,
                                       command_template=snmpv2.DISABLE_SNMP,
                                       action_map=action_map,
                                       error_map=error_map).execute_command()

    def unset_read_community(self, snmp_community, action_map=None, error_map=None):
        """

        :param snmp_community:
        :param action_map:
        :param error_map:
        :return:
        """
        return CommandTemplateExecutor(cli_service=self._cli_service,
                                       command_template=snmpv2.UNSET_READ_COMMUNITY,
                                       action_map=action_map,
                                       error_map=error_map).execute_command(snmp_community=snmp_community)

    def unset_write_community(self, snmp_community, action_map=None, error_map=None):
        """

        :param snmp_community:
        :param action_map:
        :param error_map:
        :return:
        """
        return CommandTemplateExecutor(cli_service=self._cli_service,
                                       command_template=snmpv2.UNSET_WRITE_COMMUNITY,
                                       action_map=action_map,
                                       error_map=error_map).execute_command(snmp_community=snmp_community)
