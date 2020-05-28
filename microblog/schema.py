from datetime import datetime
from typing import Optional, List

from pydantic.main import BaseModel

from user.schema import User


class PostBase(BaseModel):
    title: str
    text: str
    date: datetime


class PostList(PostBase):
    id: int
    parent_id: Optional[int] = None


class PostSingle(PostList):
    children: Optional[List[PostBase]] = None
    user: Optional[User] = None


class PostCreate(PostBase):
    parent_id: Optional[int] = None

    class Config:
        orm_mode = True
