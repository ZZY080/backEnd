from typing import List, Optional, Type

from peewee import Model, MySQLDatabase
from playhouse.kv import KeyValue

from module.database_table.file_model import FileModel
from module.database_table.transaction_model import TransactionModel
from module.database_table.user_model import UserModel
from module.global_dict import Global
from module.logger_ex import LoggerEx, LogLevel
from module.singleton_type import SingletonType


class Database(MySQLDatabase, metaclass=SingletonType):
    def sequence_exists(self, seq):
        raise NotImplementedError

    def __init__(self):
        self.config = Global().user_config.mysql_config
        super().__init__(
            self.config.database,
            host=self.config.host,
            port=self.config.port,
            user=self.config.username,
            password=self.config.password,
        )
        self.log = LoggerEx(self.__class__.__name__)
        if Global().debug_mode:
            self.log.set_level(LogLevel.DEBUG)
        self.log.debug(f'{self.__class__.__name__} initializing...')
        self.tables: List[Type[Model]] = [UserModel, TransactionModel, FileModel]  # 表名
        self.bind(self.tables)
        self.KV: Optional[KeyValue] = None  # 键值对表

    def connect(self, *args) -> bool:
        try:
            if super().connect():
                self.log.debug('connected')
            else:
                self.log.error('connection failed')
                raise ConnectionError('connection failed')
        except Exception as e:
            self.log.exception(e)
            raise e
        else:
            self.create_tables(self.tables)
            self.KV = KeyValue(database=self, table_name='kv')
            return True

    def close(self) -> bool:
        if isinstance(self.KV, KeyValue):
            self.KV = None
        if super().close():
            self.log.debug('disconnected')
            return True
        else:
            self.log.error('disconnect failed')
            return False
