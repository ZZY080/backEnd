from uuid import uuid4

from peewee import CharField, DecimalField

from module.database_table.base_table import BaseTable


class TransactionModel(BaseTable):
    id: str = CharField(primary_key=True, unique=True)  # 交易ID
    payer: str = CharField()  # 付款人
    payee: str = CharField()  # 收款人
    amount: float = DecimalField(max_digits=40, decimal_places=2, default=0.0)  # 交易金额
    remark: str = CharField(null=True)  # 备注

    class Meta:
        table_name = 'transaction'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.id:
            _id = uuid4().hex
            while self.get_transaction_by_id(_id):
                _id = uuid4().hex
            self.id = _id

    @classmethod
    def get_transaction_by_id(cls, transaction_id: str) -> 'TransactionModel':
        """通过交易ID获取交易"""
        return cls.get_or_none(cls.id == transaction_id)

    @classmethod
    def get_transaction_list(cls, username: str, page_size: int, page_index: int) -> list:
        """获取交易列表"""
        return list(cls.select()
                    .where((cls.payer == username) | (cls.payee == username))
                    .order_by(cls.created_at.desc())
                    .paginate(page_index, page_size)
                    )

    @classmethod
    def get_transaction_count(cls, username: str) -> int:
        """获取交易数量"""
        return cls.select().where((cls.payer == username) | (cls.payee == username)).count()
