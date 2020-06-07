from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, sql
from sqlalchemy.orm import relationship, backref

from core.db import Base


class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(350))
    date = Column(DateTime(timezone=True), server_default=sql.func.now())
    user_id = Column(String, ForeignKey('user.id'))
    user = relationship("User")
    parent_id = Column(Integer, ForeignKey('posts.post_id', ondelete='CASCADE'), nullable=True)
    children = relationship("Post",
                            backref=backref('parent', remote_side=[post_id], passive_deletes=True))


posts = Post.__table__
