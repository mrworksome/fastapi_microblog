from typing import Optional
from uuid import UUID

from fastapi_users import models
from pydantic import BaseModel


class User(models.BaseUser):
    name: str

    class Config:
        orm_mode = True


class UserCreate(User, models.BaseUserCreate):
    pass


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass


class UserInResponse(BaseModel):
    id: UUID
    name: Optional[str]
    email: str
