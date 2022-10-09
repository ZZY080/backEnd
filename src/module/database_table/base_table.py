from datetime import datetime
from typing import Optional, Union

from peewee import DateTimeField, Model


class BaseTable(Model):
    created_at: datetime = DateTimeField(default=datetime.now, null=True)
    updated_at: datetime = DateTimeField(default=datetime.now, null=True)

    # noinspection PyMethodOverriding
    def save(self, update=False) -> Union[bool, int]:
        if update:
            self.updated_at = datetime.now()
        return super().save(not update)

    @classmethod
    def get_by_id(cls, pk) -> Optional['BaseTable']:
        return cls.get_or_none(cls._meta.primary_key == pk)
