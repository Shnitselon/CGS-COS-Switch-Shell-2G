from cloudshell.devices.autoload.autoload_builder import AutoloadDetailsBuilder
from cloudshell.devices.standards.networking.autoload_structure import GenericResource


class CgsSNMPAutoload(object):
    def __init__(self, snmp_handler, shell_name, shell_type, resource_name, logger):
        """

        :param snmp_handler:
        :param shell_name:
        :param shell_type:
        :param resource_name:
        :param logger:
        """
        self.snmp_handler = snmp_handler
        self.shell_name = shell_name
        self.shell_type = shell_type
        self.resource_name = resource_name
        self.logger = logger
        self.elements = {}
        # self.snmp_handler.set_snmp_errors(self.SNMP_ERRORS)
        self.resource = GenericResource(shell_name=shell_name,
                                        shell_type=shell_type,
                                        name=resource_name,
                                        unique_id=resource_name)

    def discover(self, supported_os):
        """General entry point for autoload, read device structure and attributes: chassis, modules, submodules, ports,

        port-channels and power supplies
        :return: AutoLoadDetails object
        """
        return AutoloadDetailsBuilder(self.resource).autoload_details()
