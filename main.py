from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Todo(BaseModel):
    id: int
    task: str

todos = [
    { "id": 1, "task": "string 1" },
    { "id": 2, "task": "string 2" },
    { "id": 3, "task": "string 3" },
]


# index 
@app.get("/")
def read_root():
    return 'Hello from fastapi index'


# get all todos
@app.get("/todos")
def get_todos():
    return todos


# get specific todo
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    return {'msg': 'todo not found'}


# create todo
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo.dict())
    return todos


# update todo 
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: Todo):
    i = 0
    while i < len(todos):
        if todos[i]['id'] == todo_id:
            todos[i] = todo
            return todos
        i += 1 
    return {'msg': 'todo not found'}


# delete todo 
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    i = 0
    while i < len(todos):
        if todos[i]['id'] == todo_id:
            del todos[i]
            return todos
        i += 1 
    return {'msg': 'todo not found'}



