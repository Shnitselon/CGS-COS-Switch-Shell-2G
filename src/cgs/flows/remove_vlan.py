import re

from cloudshell.cli.session.session_exceptions import CommandExecutionException
from cloudshell.devices.flows.cli_action_flows import RemoveVlanFlow

from cgs.command_actions.commit import CommitActions
from cgs.command_actions.vlan import VlanActions
from cgs.errors import FilterDoesNotExist


class CgsRemoveVlanFlow(RemoveVlanFlow):
    @staticmethod
    def _get_port_name(full_port_name):
        """

        :param full_port_name:
        :return:
        """
        return re.sub("[^0-9]", "", full_port_name.split("/")[-1])

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

        with self._cli_handler.get_cli_service(self._cli_handler.enable_mode) as enable_session:
            vlan_actions = VlanActions(cli_service=enable_session, logger=self._logger)
            commit_actions = CommitActions(cli_service=enable_session, logger=self._logger)

            if port_mode == "trunk":
                filter_ids = vlan_actions.get_trunk_vlan_filters_id(port=port,
                                                                    vlan_range=vlan_range,
                                                                    action_map=action_map,
                                                                    error_map=error_map)
            else:
                filter_ids = vlan_actions.get_access_vlan_filters_id(port=port,
                                                                     vlan=vlan_range,
                                                                     action_map=action_map,
                                                                     error_map=error_map)

            if not filter_ids:
                raise FilterDoesNotExist("Unable to find filter for port {} VLAN {}".format(port, vlan_range))

            with enable_session.enter_mode(self._cli_handler.config_mode):
                try:
                    vlan_actions.remove_filters(filter_ids=filter_ids)
                    output = commit_actions.commit()
                except CommandExecutionException:
                    self._logger.exception("Failed to remove VLAN:")
                    commit_actions.abort()
                    raise

                return output
