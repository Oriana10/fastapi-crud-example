from fastapi.testclient import TestClient
from app import models
from app.main import app
from app.database import SessionLocal, engine


# Crear base de datos en memoria para pruebas
models.Base.metadata.create_all(bind=engine)

client = TestClient(app)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_item():
    response = client.post("/items/", json={"name": "Item 1", "description": "Test Item"})
    assert response.status_code == 200
    assert response.json()["name"] == "Item 1"
    assert response.json()["description"] == "Test Item"

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_item():
    item = client.post("/items/", json={"name": "Item 1", "description": "Test Item"})
    item_id = item.json()["id"]
    response = client.put(f"/items/{item_id}", json={"name": "Updated Item", "description": "Updated Description"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Item"
    assert response.json()["description"] == "Updated Description"

def test_delete_item():
    item = client.post("/items/", json={"name": "Item 1", "description": "Test Item"})
    item_id = item.json()["id"]
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Item 1"
