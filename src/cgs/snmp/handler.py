from cloudshell.devices.snmp_handler import SnmpHandler

from cgs.flows.disable_snmp import CgsDisableSnmpFlow
from cgs.flows.enable_snmp import CgsEnableSnmpFlow


class CgsSnmpHandler(SnmpHandler):
    def __init__(self, resource_config, logger, api, cli_handler):
        """

        :param resource_config:
        :param logger:
        :param api:
        :param cli_handler:
        """
        super(CgsSnmpHandler, self).__init__(resource_config, logger, api)
        self.cli_handler = cli_handler

    def _create_enable_flow(self):
        """

        :rtype: CgsEnableSnmpFlow
        """
        return CgsEnableSnmpFlow(cli_handler=self.cli_handler,
                                 resource_config=self.resource_config,
                                 logger=self._logger)

    def _create_disable_flow(self):
        """

        :rtype: CgsDisableSnmpFlow
        """
        return CgsDisableSnmpFlow(cli_handler=self.cli_handler,
                                  resource_config=self.resource_config,
                                  logger=self._logger)