from cloudshell.devices.runners.configuration_runner import ConfigurationRunner

from cgs.flows.restore import CgsRestoreFlow
from cgs.flows.save import CgsSaveFlow


class CgsConfigurationRunner(ConfigurationRunner):
    @property
    def restore_flow(self):
        return CgsRestoreFlow(cli_handler=self.cli_handler, logger=self._logger)

    @property
    def save_flow(self):
        return CgsSaveFlow(cli_handler=self.cli_handler, logger=self._logger)

    @property
    def file_system(self):
        return "fake"


    def restore(self, path, configuration_type="running", restore_method="override", vrf_management_name=None):
        """Restore configuration on device from provided configuration file
        Restore configuration from local file system or ftp/tftp server into 'running-config' or 'startup-config'.
        :param path: relative path to the file on the remote host tftp://server/sourcefile
        :param configuration_type: the configuration type to restore (StartUp or Running)
        :param restore_method: override current config or not
        :param vrf_management_name: Virtual Routing and Forwarding management name
        :return: exception on crash
        """

        if hasattr(self.resource_config, "vrf_management_name"):
            vrf_management_name = vrf_management_name or self.resource_config.vrf_management_name

        self._validate_configuration_type(configuration_type)
        import ipdb;ipdb.set_trace()
        path = self.get_path(path)

        self.restore_flow.execute_flow(path=path,
                                       configuration_type=configuration_type.lower(),
                                       restore_method=restore_method.lower(),
                                       vrf_management_name=vrf_management_name)