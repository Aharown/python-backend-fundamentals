# python-backend-fundamentals

Exercises in FastAPI, SQLAlchemy, and pytest, built ahead of the Trust & Safety Case Triage API.

Done to get an understanding of the Python backend stack into my hands before touching the real project. Separate from `python-fundamentals`, which covers CS50P specifically.

---

## Why this exists

Coming from Rails (ActiveRecord, RSpec, service objects), the goal is to build enough familiarity with the Python equivalents that the flagship project's core logic, the state machine and routing, is written with real understanding rather than translated Rails or Claude Code output I haven't internalised.

---

## Structure

Each exercise lives in its own folder with its own README noting what it covered and anything that felt different from Rails.

```
python-backend-fundamentals/
  todo-api/          FastAPI basics: routes, Pydantic models, dependency injection
  book-tracker-api/  SQLAlchemy: models, relationships, Alembic migrations

```

---

## Stack

FastAPI, SQLAlchemy, Alembic, Pydantic, pytest, PostgreSQL
