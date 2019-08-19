from cloudshell.devices.runners.state_runner import StateRunner

from cgs.flows.shutdown import CgsShutdownFlow


class CgsStateRunner(StateRunner):
    @property
    def shutdown_flow(self):
        """
        :return:
        """
        return CgsShutdownFlow(cli_handler=self.cli_handler, logger=self._logger)

    def shutdown(self):
        """
        :return:
        """
        return self.shutdown_flow.execute_flow()
