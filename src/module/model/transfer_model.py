from typing import Optional

from pydantic import BaseModel, Field


class TransferModel(BaseModel):
    target_username: str = Field(..., example='user2')
    amount: float = Field(..., example=2.34)
    remark: Optional[str] = Field(None, example='这是备注')

