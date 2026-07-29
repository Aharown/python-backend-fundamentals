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


