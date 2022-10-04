from threading import Thread

import uvicorn as uvicorn

from module.constants import APP_NAME, AUTHOR_NAME
from module.database import Database
from module.exception_ex import PortInUseError
from module.global_dict import Global
from module.http_server import HttpServer
from module.logger_ex import LoggerEx, LogLevel
from module.singleton_type import SingletonType
from module.utility import is_port_in_use, kill_thread


class CreativePay(metaclass=SingletonType):
    def __init__(self):
        self.log = LoggerEx(self.__class__.__name__)
        if Global().debug_mode:
            self.log.set_level(LogLevel.DEBUG)

        self.config = Global().user_config.server_config
        # 一定要严格按照顺序初始化，否则可能会出现异常
        self.database = Database()
        self.http_app = HttpServer()
        self.http_thread = None

        # 打印版本信息
        self.log.info(f'{APP_NAME} By {AUTHOR_NAME}')

    def start(self):
        """启动CreativePay"""
        if is_port_in_use(self.config.port):  # 检查端口是否被占用
            raise PortInUseError(f'Port {self.config.port} already in use')
        self.database.connect()  # 连接数据库
        self.http_thread = Thread(
            target=uvicorn.run,
            daemon=True,
            kwargs={
                'app': self.http_app,
                'host': self.config.host,
                'port': self.config.port,
                'log_level': 'warning' if Global().debug_mode else 'critical',
            }
        )
        self.http_thread.start()  # 启动HTTP服务

    def stop(self):
        """停止CreativePay"""
        self.log.debug(f'{APP_NAME} stopping.')
        if isinstance(self.http_thread, Thread) and self.http_thread.is_alive():
            kill_thread(self.http_thread)
        self.log.info(f'{APP_NAME} stopped, see you next time.')
