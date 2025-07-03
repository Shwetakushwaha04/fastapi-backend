from tortoise.contrib.pydantic import pydantic_model_creator

from models.todo import Todo

TodoPydantic= pydantic_model_creator(Todo, name = "Todo")
TodoInPydantic= pydantic_model_creator(Todo, name = "TodoIn",exclude=['user_id', 'active'], exclude_readonly=True)

