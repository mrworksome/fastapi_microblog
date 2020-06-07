import uvicorn
from fastapi import FastAPI

from core.db_utils import create_db_client, shutdown_db_client
from microblog.blog import router as blog_router
from user.routers import routes as user_routes

app = FastAPI()

app.add_event_handler("startup", create_db_client)
app.add_event_handler("shutdown", shutdown_db_client)

app.include_router(blog_router, prefix='/blog')
app.include_router(user_routes)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
