from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Category(Enum):
    PERSONAL = 'personal'
    WORK = 'work'
    
class Todo(BaseModel):
    title: str
    completed: bool
    id: int
    category: Category

todos = {
    0: Todo(title="test1", completed=True, id=0, category=Category.PERSONAL),
    1: Todo(title="test2", completed=False, id=1, category=Category.WORK)
}

@app.get('/')
def index() -> dict[str, dict[int, Todo]]:
    return {"todos": todos}

'''
@app.get('/todos/{todo_id}')
def get_todo_by_id(todo_id: int) -> Todo:
    return todos[todo_id]'''
