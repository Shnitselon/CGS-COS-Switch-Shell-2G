from cloudshell.devices.flows.cli_action_flows import ShutdownFlow

from cgs.command_actions.state import StateActions


class CgsShutdownFlow(ShutdownFlow):
    def execute_flow(self):
        """

        :return:
        """
        with self._cli_handler.get_cli_service(self._cli_handler.enable_mode) as cli_service:
            state_actions = StateActions(cli_service=cli_service, logger=self._logger)
            return state_actions.shutdown()
