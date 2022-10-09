from module.constants import COMMAND_HELP_TEXT
from module.global_dict import Global
from module.logger_ex import LoggerEx, LogLevel
from module.singleton_type import SingletonType


class CommandHandler(metaclass=SingletonType):
    def __init__(self):
        self.log = LoggerEx(self.__class__.__name__)
        if Global().debug_mode:
            self.log.set_level(LogLevel.DEBUG)

    def add(self, command: str) -> None:
        """接收指令

        :param command: 指令
        """
        self.log.debug(f'Get command: {command}')
        if command in {'/help', '/h', '?', '/?', '？'}:
            self.log.print(COMMAND_HELP_TEXT)
        elif command == '/exit':
            Global().time_to_exit = True
        else:
            self.log.error('Invalid Command')
