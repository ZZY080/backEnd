from pydantic import BaseModel


class CheckUsernameValidModel(BaseModel):
    username: str
