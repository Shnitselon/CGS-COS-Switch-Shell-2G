from cloudshell.cli.session.session_exceptions import CommandExecutionException
from cloudshell.devices.flows.cli_action_flows import RemoveVlanFlow

from cgs.command_actions.commit import CommitActions
from cgs.command_actions.vlan import VlanActions


class CgsRemoveVlanFlow(RemoveVlanFlow):
    @staticmethod
    def _get_port_name(full_port_name):
        """

        :param full_port_name:
        :return:
        """
        return full_port_name.split("/")[-1]

    def execute_flow(self, vlan_range, port_name, port_mode, action_map=None, error_map=None):
        """

        :param vlan_range:
        :param port_name:
        :param port_mode:
        :param action_map:
        :param error_map:
        :return:
        """
        port = self._get_port_name(full_port_name=port_name)

        with self._cli_handler.get_cli_service(self._cli_handler.config_mode) as cli_service:
            vlan_actions = VlanActions(cli_service=cli_service, logger=self._logger)
            commit_actions = CommitActions(cli_service=cli_service, logger=self._logger)

            try:
                if port_mode == "trunk":
                    # todo: show filters command should be triggered in the ENABLE mode !!!
                    output = vlan_actions.remove_trunk_vlan_filter(port=port, vlan_range=vlan_range)
                else:
                    output = vlan_actions.remove_access_vlan_filter(port=port, vlan=vlan_range)

                output += commit_actions.commit()

            except CommandExecutionException:
                self._logger.exception("Failed to remove VLAN:")
                commit_actions.abort()
                raise

        return output