from datetime import datetime
from typing import Union

from peewee import CharField, DateTimeField

from module.database_table.base_table import BaseTable


class UserModel(BaseTable):
    username: str = CharField(primary_key=True, unique=True)
    password: str = CharField()
    nickname: str = CharField(null=True)

    created_at: datetime = DateTimeField(default=datetime.now, null=True)
    updated_at: datetime = DateTimeField(default=datetime.now, null=True)

    class Meta:
        table_name = 'user'

    # noinspection PyMethodOverriding
    def save(self, update=False) -> Union[bool, int]:
        if update:
            self.updated_at = datetime.now()
        return super().save(not update)

    @classmethod
    def is_username_exist(cls, username: str) -> bool:
        """判断用户名是否存在"""
        return cls.select().where(cls.username == username).count() > 0

    @classmethod
    def is_password_correct(cls, username: str, password: str) -> bool:
        """判断密码是否正确"""
        return cls.get_or_none(cls.username == username, cls.password == password) is not None
