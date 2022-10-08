from uuid import uuid4

from peewee import BooleanField, CharField, IntegerField

from module.database_table.base_table import BaseTable


class FileModel(BaseTable):
    id: str = CharField(primary_key=True, unique=True)
    name: str = CharField()  # 文件名
    type: str = CharField()  # 文件类型
    size: int = IntegerField()  # 文件大小
    hash: str = CharField()  # 文件哈希
    enable: bool = BooleanField(default=True)  # 是否可用

    class Meta:
        table_name = 'file'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.id:
            _id = uuid4().hex
            while self.get_by_id(_id):
                _id = uuid4().hex
            self.id = _id

    @classmethod
    def get_by_hash(cls, file_hash: str) -> 'FileModel':
        """通过文件哈希获取文件"""
        return cls.get_or_none(cls.hash == file_hash)
