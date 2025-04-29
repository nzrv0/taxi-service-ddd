from pydantic import BaseModel

class BaseUser(BaseModel):
    name: str


class User(BaseUser):
    surname: str

user = User()