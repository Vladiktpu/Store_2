import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_create_product(client):
    response = client.post("/products", json={
        "name": "Тестовый товар",
        "description": "Описание",
        "price": 1000,
        "stock": 5
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Тестовый товар"

def test_get_products(client):
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_product_by_id(client):
    create_response = client.post("/products", json={
        "name": "Товар по ID",
        "description": "Описание",
        "price": 750,
        "stock": 10
    })
    product_id = create_response.json()["id"]
    
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["id"] == product_id

def test_update_product(client):
    create_response = client.post("/products", json={
        "name": "Старое имя",
        "description": "Описание",
        "price": 100,
        "stock": 1
    })
    product_id = create_response.json()["id"]
    
    response = client.put(f"/products/{product_id}", json={
        "name": "Новое имя",
        "price": 200
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Новое имя"
    assert data["price"] == 200

def test_delete_product(client):
    create_response = client.post("/products", json={
        "name": "Товар на удаление",
        "description": "Описание",
        "price": 300,
        "stock": 2
    })
    product_id = create_response.json()["id"]
    
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200
    
    get_response = client.get(f"/products/{product_id}")
    assert get_response.status_code == 404