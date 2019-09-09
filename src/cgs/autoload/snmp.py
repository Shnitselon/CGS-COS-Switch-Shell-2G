import re
import os

from cgs.autoload.snmp_if_table import SnmpIfTable

from cloudshell.devices.autoload.autoload_builder import AutoloadDetailsBuilder
from cloudshell.devices.standards.networking.autoload_structure import *


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
        self.resource = GenericResource(shell_name=shell_name,
                                        shell_type=shell_type,
                                        name=resource_name,
                                        unique_id=resource_name)

        self.chassis = GenericChassis(shell_name=self.shell_name,
                                      name="Chassis",
                                      unique_id="{}.{}".format(self.resource_name, "chassis"))

        self.resource.add_sub_resource("1", self.chassis)

    def _load_mibs(self):
        """Load CGS specific MIBs inside SNMP handler"""
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "mibs"))
        self.snmp_handler.update_mib_sources(path)

    def discover(self, supported_os):
        """General entry point for autoload, read device structure and attributes:

        chassis, modules, submodules, ports, port-channels and power supplies
        :return: AutoLoadDetails object
        """
        self.logger.info("*" * 70)
        self.logger.info("Start SNMP discovery process .....")
        self._load_mibs()
        self._get_device_details()
        self._load_snmp_tables()
        self._build_ports()

        autoload_details = AutoloadDetailsBuilder(self.resource).autoload_details()
        self._log_autoload_details(autoload_details)

        return autoload_details

    def _log_autoload_details(self, autoload_details):
        """Logging autoload details

        :param autoload_details:
        :return:
        """
        self.logger.debug("-------------------- <RESOURCES> ----------------------")
        for resource in autoload_details.resources:
            self.logger.debug(
                "{0:15}, {1:20}, {2}".format(resource.relative_address, resource.name, resource.unique_identifier))
        self.logger.debug("-------------------- </RESOURCES> ----------------------")

        self.logger.debug("-------------------- <ATTRIBUTES> ---------------------")
        for attribute in autoload_details.attributes:
            self.logger.debug("-- {0:15}, {1:60}, {2}".format(attribute.relative_address, attribute.attribute_name,
                                                              attribute.attribute_value))
        self.logger.debug("-------------------- </ATTRIBUTES> ---------------------")

    def _get_device_model(self):
        """Get device model from the SNMPv2 mib
        :return: device model
        :rtype: str
        """
        result = ''
        match_name = re.search(r'::(?P<model>\S+$)', self.snmp_handler.get_property('SNMPv2-MIB', 'sysObjectID', '0'))
        if match_name:
            result = match_name.group('model')

        return result

    def _get_device_details(self):
        """Get root element attributes """

        self.logger.info("Building Root")
        vendor = "CGS"

        self.resource.contact_name = self.snmp_handler.get_property('SNMPv2-MIB', 'sysContact', '0')
        self.resource.system_name = self.snmp_handler.get_property('SNMPv2-MIB', 'sysName', '0')
        self.resource.location = self.snmp_handler.get_property('SNMPv2-MIB', 'sysLocation', '0')
        self.resource.model = self.resource.model_name = self._get_device_model()
        self.resource.vendor = vendor

    def _load_snmp_tables(self):
        """Load all Cisco required snmp tables

        :return:
        """
        self.logger.info("Start loading ifTable MIB")
        self.if_table = SnmpIfTable(snmp_handler=self.snmp_handler, logger=self.logger)
        self.logger.info("fTable MIB loaded")

    def _build_ports(self):
        """Get resource details and attributes for every port in self.port_list

        :return:
        """
        self.logger.info("Loading Ports:")

        for if_port in self.if_table.if_ports:
            port = GenericPort(shell_name=self.shell_name,
                               name=if_port.if_name.replace("/", "-"),
                               unique_id="{0}.{1}.{2}".format(self.resource_name, "port", if_port.if_index))

            port.mac_address = if_port.if_mac
            port.l2_protocol_type = if_port.if_type
            port.ipv4_address = if_port.ipv4_address
            port.ipv6_address = if_port.ipv6_address
            port.port_description = if_port.if_port_description
            port.bandwidth = if_port.if_speed
            port.mtu = if_port.if_mtu
            port.duplex = if_port.duplex
            port.adjacent = if_port.adjacent
            port.auto_negotiation = if_port.auto_negotiation
            self.chassis.add_sub_resource(if_port.if_index, port)
            self.logger.info("Added port {}".format(if_port.if_index))

        self.logger.info("Building Ports completed")