import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Amazon Clone" in response.data


def test_products_page():
    client = app.test_client()
    response = client.get("/products")
    assert response.status_code == 200


def test_product_detail():
    client = app.test_client()
    response = client.get("/product/1")
    assert response.status_code == 200


def test_cart_page():
    client = app.test_client()
    response = client.get("/cart")
    assert response.status_code == 200


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "UP"