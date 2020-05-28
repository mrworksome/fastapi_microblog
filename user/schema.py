from datetime import datetime

from fastapi_users import models


class User(models.BaseUser):
    name: str
    date: datetime

    class Config:
        orm_mode = True


class UserCreate(User, models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass
