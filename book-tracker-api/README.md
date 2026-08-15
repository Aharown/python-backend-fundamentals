# book-tracker-api

FastAPI + SQLAlchemy + Postgres exercise. Builds on `todo-api` by swapping in-memory storage for a real database, so the focus moves to ORM models, migrations, and the session lifecycle without changing the routing or Pydantic patterns already covered.

---

## What this covers

- A SQLAlchemy model for a Book (id, title, author, read)
- Alembic migrations to create and version the `books` table
- GET all books
- POST to create one, validated by the Pydantic model
- GET by id, 404 if not found
- PUT to update, 404 if not found
- DELETE, 404 if not found
- Tests against a separate SQLite test database, using dependency overrides so the real Postgres database isn't touched
---

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
createdb book_tracker
alembic upgrade head
uvicorn app.main:app --reload
```

---

## Notes

- Postgres databases aren't files. `createdb` creates a named space inside a running server, not something you'll find in the project folder. Use `psql -l` or `psql book_tracker` to confirm it exists.
- SQLAlchemy and Alembic do two separate jobs that happen to read the same models. SQLAlchemy runs as part of the app, every request. Alembic runs separately, from the terminal, only when the schema itself changes.
- `alembic revision --autogenerate` diffs what the model classes say the schema should be against what the database actually has, and writes the migration for the difference. Always read the generated file before running it.
- Pydantic only builds itself from a dict by default. `from_attributes = True` on the response schema lets it read a SQLAlchemy model instance's attributes directly instead, since the ORM returns objects, not dicts.
- `get_db` uses `yield` instead of `return` so the session gets cleaned up automatically after each request, success or failure.
- Creating a row is three steps, not one. `db.add()` stages it in memory, `db.commit()` writes it to Postgres, and `db.refresh()` reads it back so the Python object picks up the id Postgres generated, since that id doesn't exist in memory until commit actually happens.
- `HTTPException` is for a specific, meaningful client-facing failure, like an id that doesn't exist. It's not needed on GET-all, since an empty list is a valid result, not an error.
- Tests run against a disposable SQLite database, not Postgres. `app.dependency_overrides[get_db]` swaps in a test session everywhere the app expects the real one, without touching any route code.
