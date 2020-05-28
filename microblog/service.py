from sqlalchemy import and_, union, except_, select, union_all
from sqlalchemy.orm import aliased

from core.db import database
from microblog.model import posts, Post
from microblog.schema import PostCreate, PostSingle
from user.logic import users
from user.schema import User
from user.model import User as usr



async def get_post_list():
    return await database.fetch_all(query=posts.select())


async def create_post(item: PostCreate, user: User):
    post = posts.insert().values(**item.dict(), user=user.id)
    return await database.execute(post)


async def get_post(pk: int):
    post_single = await database.fetch_one(query=posts.select().where(posts.c.id == pk))
    post_children = await database.fetch_all(query=posts.select().where(posts.c.parent_id == pk))
    user_id = dict(post_single).get('user')
    user = await database.fetch_one(query=users.select().where(users.c.id == user_id))
    ps = PostSingle(**post_single)
    ps.user = User(**user)
    ps.children = post_children

    # x = await database.fetch_all(
    #     union(
    #         posts.join(users).select().where(
    #             and_(
    #                 posts.c.id == pk,
    #                 users.c.id == posts.c.user,
    #             )
    #         ),
    #         posts.join(users).select().where(and_(posts.c.parent_id == pk, users.c.id == posts.c.user))
    #     )
    # )
    # [print(dict(a)) for a in x]
    a = 1
    return ps
