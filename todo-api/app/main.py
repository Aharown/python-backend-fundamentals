from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
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


@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos_db[todo_id]


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo: TodoCreate):
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    updated = Todo(id=todo_id, title=todo.title, done=todo.done)
    todos_db[todo_id] = updated
    return updated


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos_db[todo_id]
    return {"message": "Todo deleted"}
