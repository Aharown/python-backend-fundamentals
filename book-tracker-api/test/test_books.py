def test_create_book(client):
    response = client.post("/books", json={"title": "Dune", "author": "Frank Herbert"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Dune"
    assert data["read"] is False
    assert "id" in data

def test_get_books_empty(client):
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == []

def test_get_book_not_found(client):
    response = client.get("/books/999")
    assert response.status_code == 404

def test_get_book_by_id(client):
    created = client.post("/books", json={"title": "Dune", "author": "Frank Herbert"}).json()
    response = client.get(f"/books/{created['id']}")
    assert response.status_code == 200
    assert response.json()["title"] == "Dune"

def test_update_book(client):
    created = client.post("/books", json={"title": "Dune", "author": "Frank Herbert"}).json()
    response = client.put(
        f"/books/{created['id']}",
        json={"title": "Dune", "author": "Frank Herbert", "read": True}
    )
    assert response.status_code == 200
    assert response.json()["read"] is True

def test_delete_book(client):
    created = client.post("/books", json={"title": "Dune", "author": "Frank Herbert"}).json()
    response = client.delete(f"/books/{created['id']}")
    assert response.status_code == 204

    follow_up = client.get(f"/books/{created['id']}")
    assert follow_up.status_code == 404

def test_get_book_invalid_id_type(client):
    response = client.get("/books/not-a-number")
    assert response.status_code == 422  

def test_update_book_not_found(client):
    response = client.put(
        "/books/999",
        json={"title": "Dune", "author": "Frank Herbert", "read": False}
    )
    assert response.status_code == 404

def test_delete_book_not_found(client):
    response = client.delete("/books/999")
    assert response.status_code == 404
