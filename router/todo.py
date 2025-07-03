from typing import List
from fastapi import APIRouter

from models.todo import Todo
from schemas.todo import TodoInPydantic, TodoPydantic
from lib.gcu import gcu 

router = APIRouter()

@router.get("", response_model=List[TodoPydantic])
async def get_todos(cu: gcu):
  return await TodoPydantic.from_queryset(Todo.filter(user_id=cu.id))


@router.post("", response_model=TodoPydantic)
async def add_todo(todo: TodoInPydantic, cu: gcu): # type: ignore
  todo_obj = await Todo.create(title=todo.title, desc=todo.desc, user_id=cu.id)
  return await TodoPydantic.from_tortoise_orm(todo_obj)

TodoRouter = router
