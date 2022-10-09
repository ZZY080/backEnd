import platform
from pathlib import Path
from typing import TYPE_CHECKING, Optional

import psutil

from module.constants import APP_NAME
from module.server_status import ServerStatus
from module.singleton_type import SingletonType
from module.utility import (get_script_memory_usage, get_script_uptime,
                            get_system_description, get_system_memory_usage,
                            get_system_uptime)

if TYPE_CHECKING:
    from creative_pay import CreativePay as App
    from module.command_handler import CommandHandler
    from module.database import Database
    from module.user_config import UserConfig


class Global(metaclass=SingletonType):
    """全局变量，单例模式"""

    ############
    # 全局的变量 #
    ############

    exit_code = 0  # 退出码
    time_to_exit = False  # 是时候退出了
    debug_mode = False  # 调试模式

    ############
    # 共享的对象 #
    ############

    user_config: 'UserConfig' = None  # 用户配置
    database: 'Database' = None  # 数据库
    command_handler: 'CommandHandler' = None  # 命令处理器
    app: Optional['App'] = None  # 应用程序

    args_known = ()  # 命令行参数
    args_unknown = ()  # 未知命令

    ############
    # 目录与路径 #
    ############

    root_dir = Path('.')  # 根目录
    data_dir = Path(root_dir, 'data')  # 数据目录

    def __init__(self):
        # 创建目录
        for dir_ in [self.data_dir]:
            dir_.mkdir(parents=True, exist_ok=True)

    @property
    def information(self) -> ServerStatus:
        """获取应用信息"""
        return ServerStatus(
            python_version=platform.python_version(),
            system_description=get_system_description(),

            system_cpu_present=psutil.cpu_percent(),
            system_memory_usage=get_system_memory_usage(),
            app_memory_usage=get_script_memory_usage(),

            system_uptime=get_system_uptime(),
            app_uptime=get_script_uptime(),

            app_name=APP_NAME,
        )


if __name__ == '__main__':
    ...
