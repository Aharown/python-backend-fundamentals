from fastapi import FastAPI
from app.schemas import Todo

app = FastAPI()

todos_db: dict[int, Todo] = {}

@app.get("/todos", response_model=list[Todo])
def get_todos():
    return list(todos_db.values())
