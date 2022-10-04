from module.config_entity.mysql_config import MysqlConfig
from module.config_entity.server_config import ServerConfig
from module.global_dict import Global
from module.logger_ex import LoggerEx, LogLevel
from module.singleton_type import SingletonType
from module.yaml_config import YamlConfig
import os


class UserConfig(metaclass=SingletonType):
    server_config = ServerConfig()  # 服务器配置
    mysql_config = MysqlConfig()  # 数据库配置

    config_data: YamlConfig = {}

    def __init__(self, file_path):
        self.log = LoggerEx(self.__class__.__name__)
        self.file_path = file_path
        if Global().debug_mode:
            self.log.set_level(LogLevel.DEBUG)
        self.load()
        self.server_config.save = self.save
        self.mysql_config.save = self.save

    def load(self) -> None:
        self.log.debug(f'Loading config file: {self.file_path}')
        self.config_data = YamlConfig(self.file_path)
        need_save = len(self.config_data) == 0

        # 读取环境变量
        env = os.environ
        env_dict = {}
        for key in env:
            if key.startswith('CP_') and len(key) > 3:
                env_dict[key[3:].lower()] = env[key]
        self.log.debug(f'Environment variables: {env_dict}')

        # 读取配置
        gg = [
            (self.server_config, 'server'),
            (self.mysql_config, 'mysql'),
        ]
        for g in gg:
            t = dict(self.config_data.get(g[1]))
            for key in env_dict:
                if key.startswith(g[1] + '_'):
                    t[key[len(g[1]) + 1:]] = env_dict[key]
            g[0].update(t)
            if len(t) < len(g[0]):
                need_save = True

        # 若配置项不存在，则创建配置项
        self.config_data['server'] = self.server_config.to_dict()
        self.config_data['mysql'] = self.mysql_config.to_dict()

        self.log.debug(f'Config loaded: {dict(self.config_data)}')
        if need_save:
            self.save()

    def save(self) -> None:
        self.log.debug(f'Saving config file: {self.file_path}')
        self.config_data['server'] = self.server_config.to_dict()
        self.config_data['mysql'] = self.mysql_config.to_dict()
        self.config_data.save()  # TODO: 写出时保留注释
        self.log.debug(f'Config saved: {dict(self.config_data)}')
