from cloudshell.cli.command_mode import CommandMode

# new line or begin of the line that doesn't saved in match
BEGIN_LINE_PATTERN = r"((?<=\n)|^)"
CONFIG_MODE_PROMPT_TPL = r"{}\S+\({{}}\)#\s*$".format(BEGIN_LINE_PATTERN)


class EnableCommandMode(CommandMode):
    PROMPT = r"{}.*[^\)]#\s*$".format(BEGIN_LINE_PATTERN)
    ENTER_COMMAND = ""
    EXIT_COMMAND = "exit"

    def __init__(self, resource_config, api):
        """Initialize Enable command mode

        :param resource_config:
        """
        self.resource_config = resource_config
        self._api = api

        super(EnableCommandMode, self).__init__(prompt=self.PROMPT,
                                                enter_command=self.ENTER_COMMAND,
                                                exit_command=self.EXIT_COMMAND)


class ConfigCommandMode(CommandMode):
    PROMPT = CONFIG_MODE_PROMPT_TPL.format("config")
    ENTER_COMMAND = "config"
    EXIT_COMMAND = "exit"

    def __init__(self, resource_config, api):
        """Initialize Config command mode

        :param resource_config:
        """
        self.resource_config = resource_config
        self._api = api

        super(ConfigCommandMode, self).__init__(prompt=self.PROMPT,
                                                enter_command=self.ENTER_COMMAND,
                                                exit_command=self.EXIT_COMMAND)


class SNMPConfigCommandMode(ConfigCommandMode):
    PROMPT = CONFIG_MODE_PROMPT_TPL.format("config-snmp")
    ENTER_COMMAND = "system snmp"
    EXIT_COMMAND = "exit"


class SNMPv3UserConfigCommandMode(ConfigCommandMode):
    PROMPT = CONFIG_MODE_PROMPT_TPL.format("config-v3-username-{}")
    ENTER_COMMAND = "v3-username {}"
    EXIT_COMMAND = "exit"

    def __init__(self, resource_config, api, username, parent_mode):
        """Initialize Config command mode

        :param resource_config:
        """
        self.resource_config = resource_config
        self._api = api

        super(ConfigCommandMode, self).__init__(
            prompt=self.PROMPT.format(username),
            enter_command=self.ENTER_COMMAND.format(username),
            exit_command=self.EXIT_COMMAND,
            parent_mode=parent_mode,
        )


class SwUpgradeConfigCommandMode(ConfigCommandMode):
    PROMPT = CONFIG_MODE_PROMPT_TPL.format("config-sw-upgrade")
    ENTER_COMMAND = "system sw-upgrade"
    EXIT_COMMAND = "exit"


CommandMode.RELATIONS_DICT = {
    EnableCommandMode: {
        ConfigCommandMode: {
            SNMPConfigCommandMode: {},
            SwUpgradeConfigCommandMode: {},
        }
    }
}
