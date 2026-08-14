# todo-api

FastAPI basics exercise. In-memory only, no database yet, so the focus stays on routing, Pydantic models, and dependency injection without SQLAlchemy muddying it.

---

## What this covers

- A Pydantic model for a Todo item (id, title, done)
- GET all todos
- POST to create one, validated by the Pydantic model
- GET by id
- PUT to update
- DELETE
---

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## Notes

- FastAPI uses TestClient to make requests to the application without an active server
- Importance of using a venv so that packages and their configurations for this project don't interact with their
counterparts outside the project
- Input/output schema split. TodoCreate doesn't include id because assigning it isn't the client's job. TodoCreate is what the client sends on POST and PUT. Todo is what gets sent back on every endpoint that returns data, including GET, since it needs the id to identify which todo it is.
