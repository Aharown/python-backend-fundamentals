from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_todos_empty():
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []

def test_create_todo():
    response = client.post("/todos", json={"title": "buy milk", "done": False})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "buy milk"
    assert data["done"] is False
    assert "id" in data

def test_get_todo_by_id():
    created = client.post("/todos", json={"title": "walk dog", "done": False}).json()
    response = client.get(f"/todos/{created['id']}")
    assert response.status_code == 200
    assert response.json()["title"] == "walk dog"

def test_get_todo_not_found():
    response = client.get("/todos/999")
    assert response.status_code == 404

def test_update_todo():
    created = client.post("/todos", json={"title": "read book", "done": False}).json()
    response = client.put(f"/todos/{created['id']}", json={"title": "read book", "done": True})
    assert response.status_code == 200
    assert response.json()["done"] is True

def test_delete_todo():
    created = client.post("/todos", json={"title": "temp", "done": False}).json()
    response = client.delete(f"/todos/{created['id']}")
    assert response.status_code == 200
    followup = client.get(f"/todos/{created['id']}")
    assert followup.status_code == 404
