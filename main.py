import jwt
from typing import Annotated
from fastapi import Depends, FastAPI

from db.db import init_db
from router.todo import TodoRouter
from router.user import UserRouter
from router.token import AuthRouter
from lib import gcu


app = FastAPI()

init_db(app)

@app.get("/")
def read_root():
  return {"info": "todo api backend", "version":"0.1.0"}

# @app.get("/users/me")
# async def read_users_me(cu: gcu):
#   return cu

app.include_router(AuthRouter, tags=['Auth'],)
app.include_router(TodoRouter, tags=['Todos'], prefix='/todos')
app.include_router(UserRouter, tags=['Users'], prefix='/users')
