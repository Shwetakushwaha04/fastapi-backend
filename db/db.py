from fastapi import FastAPI
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise 

def init_db(app : FastAPI)-> None:
    register_tortoise(
        app,
        db_url="sqlite://db.sqlite3",
        modules={"models" : ["models.todo", "models.user"]},
        generate_schemas = True,
        add_exception_handlers = True
    )
  
Tortoise.init_models(["app.models"],"models")  