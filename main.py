import uvicorn
from fastapi import FastAPI

from core.db_utils import create_db_client, shutdown_db_client

from core.fast_users import fastapi_users
from microblog.blog import router as blog_router

app = FastAPI()

app.add_event_handler("startup", create_db_client)
app.add_event_handler("shutdown", shutdown_db_client)


app.include_router(blog_router, prefix='/blog')
app.include_router(fastapi_users.router, prefix="/users", tags=["users"])




# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()
#     return response


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
