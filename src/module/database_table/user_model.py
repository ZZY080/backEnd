from datetime import datetime
from typing import Union

from peewee import CharField, DateTimeField, DecimalField

from module.database_table.base_table import BaseTable


class UserModel(BaseTable):
    username: str = CharField(primary_key=True, unique=True)  # 用户名
    password: str = CharField()  # 密码
    nickname: str = CharField(null=True)  # 昵称
    balance: float = DecimalField(max_digits=40, decimal_places=2, default=0.0)  # 余额

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

    @classmethod
    def get_user_information(cls, username: str) -> dict:
        """获取用户信息"""
        user = cls.get_or_none(cls.username == username)
        if user is None:
            return {}
        return {
            'username': user.username,
            'nickname': user.nickname,
        }

    @classmethod
    def get_user_by_name(cls, username: str) -> 'UserModel':
        """通过用户名获取用户"""
        return cls.get_or_none(cls.username == username)
