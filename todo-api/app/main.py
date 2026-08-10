from fastapi import FastAPI
from app.schemas import Todo
from app.schemas import TodoCreate, Todo


app = FastAPI()

todos_db: dict[int, Todo] = {}
next_id = 1

@app.get("/todos", response_model=list[Todo])
def get_todos():
    return list(todos_db.values())


@app.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    global next_id
    new_todo = Todo(id=next_id, title=todo.title, done=todo.done)
    todos_db[next_id] = new_todo
    next_id += 1
    return new_todo
