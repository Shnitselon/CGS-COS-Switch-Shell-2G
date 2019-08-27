from cloudshell.devices.flows.snmp_action_flows import AutoloadFlow

from cgs.autoload.snmp import CgsSNMPAutoload


class CgsSnmpAutoloadFlow(AutoloadFlow):
    def execute_flow(self, supported_os, shell_name, shell_type, resource_name):
        """

        :param supported_os:
        :param shell_name:
        :param shell_type:
        :param resource_name:
        :return:
        """
        with self._snmp_handler.get_snmp_service() as snmp_service:
            snmp_autoload = CgsSNMPAutoload(snmp_handler=snmp_service,
                                            shell_name=shell_name,
                                            shell_type=shell_type,
                                            resource_name=resource_name,
                                            logger=self._logger)

            return snmp_autoload.discover(supported_os)
