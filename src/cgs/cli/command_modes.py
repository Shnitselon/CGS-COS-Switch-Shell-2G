from cloudshell.cli.command_mode import CommandMode

# new line or begin of the line that doesn't saved in match
BEGIN_LINE_PATTERN = r"((?<=\n)|^)"


class EnableCommandMode(CommandMode):
    PROMPT = (
        r"{}".format(BEGIN_LINE_PATTERN) +
        r"((?!\(config.*?\))(\w|-|\(|\)))*"  # \w or - or () and without (config.*)
        r"#\s*$"
    )
    ENTER_COMMAND = ""
    EXIT_COMMAND = "exit"

    def __init__(self, resource_config, api):
        """Initialize Enable command mode
        :param resource_config:
        """
        self.resource_config = resource_config
        self._api = api

        super(EnableCommandMode, self).__init__(EnableCommandMode.PROMPT,
                                                EnableCommandMode.ENTER_COMMAND,
                                                EnableCommandMode.EXIT_COMMAND)


class ConfigCommandMode(CommandMode):
    # todo: verify prompt for config, config-snmp, config-snmp-testuserv3, etc
    PROMPT = r"{}\S+\(config.*\)#\s*$".format(BEGIN_LINE_PATTERN)
    ENTER_COMMAND = "config"
    EXIT_COMMAND = "exit"

    def __init__(self, resource_config, api):
        """Initialize Config command mode

        :param resource_config:
        """
        self.resource_config = resource_config
        self._api = api

        super(ConfigCommandMode, self).__init__(ConfigCommandMode.PROMPT,
                                                ConfigCommandMode.ENTER_COMMAND,
                                                ConfigCommandMode.EXIT_COMMAND)


CommandMode.RELATIONS_DICT = {
    EnableCommandMode: {
        ConfigCommandMode: {}
    }
}
