from datetime import datetime
from typing import Union

from peewee import DateTimeField, Model


class BaseTable(Model):
    created_at: datetime = DateTimeField(default=datetime.now, null=True)
    updated_at: datetime = DateTimeField(default=datetime.now, null=True)

    # noinspection PyMethodOverriding
    def save(self, update=False) -> Union[bool, int]:
        if update:
            self.updated_at = datetime.now()
        return super().save(not update)
