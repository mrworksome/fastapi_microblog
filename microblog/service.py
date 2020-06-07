from sqlalchemy import and_, union

from core.db import database
from microblog.model import posts
from microblog.schema import PostCreate, PostInDB, PostCommentList, PostBase, PostUpdate
from user.logic import users
from user.schema import User, UserInResponse


async def get_post_list():
    """ Get all posts """
    return await database.fetch_all(query=posts.select())


async def create_post(item: PostCreate, user: User) -> PostInDB:
    """ Create post """
    post = posts.insert().values(**item.dict(), user_id=str(user.id))
    pk = await database.execute(post)
    post_in_db = PostInDB(**item.dict())
    post_in_db.post_id = pk
    post_in_db.user = UserInResponse(**user.dict())

    return post_in_db


async def get_post(pk: int) -> PostCommentList:
    """ Get post with children posts """
    query = union(
        posts.join(users).select().where(and_(
            posts.c.post_id == pk, users.c.id == posts.c.user_id)),
        posts.join(users).select().where(and_(
            posts.c.parent_id == pk, users.c.id == posts.c.user_id))
    )
    current_post = None
    async for post in database.iterate(query=query):
        if pk == dict(post).get("post_id"):
            current_post = PostCommentList(**post)
            current_post.user = UserInResponse(**post)
        elif pk == dict(post).get("parent_id"):
            current_post.children.append(PostBase(**post))
    return current_post


async def update_post(pk: int, item: PostUpdate, user: User) -> PostInDB:
    """ Update post """
    post = posts.update().where(and_(
        posts.c.post_id == pk, posts.c.user_id == str(user.id))).values(**item.dict())
    await database.execute(post)
    updated_post = PostInDB(**item.dict())
    updated_post.post_id = pk
    updated_post.user = UserInResponse(**user.dict())
    return updated_post


async def delete_post(pk: int, user: User) -> None:
    """ Delete post cascade if post have a children post """
    post = posts.delete().where((posts.c.post_id == pk) & (posts.c.user_id == str(user.id)))

    return await database.execute(post)
