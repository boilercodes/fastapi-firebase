"""This is a generated example file that is supposed to be modified."""

from typing import Any, Dict

from fastapi.testclient import TestClient

from app.core import settings


def test_create_product(client: TestClient, random_product: Dict[str, Any]) -> None:
    """Test the create API."""
    response = client.post(f"{settings.api.endpoint}/products", json=random_product)
    assert response.ok


def test_read_products(client: TestClient) -> None:
    """Test the read API."""
    response = client.get(f"{settings.api.endpoint}/products")
    assert response.ok

    products = response.json()
    assert len(products) > 0


def test_update_product(client: TestClient, random_product: Dict[str, Any]) -> None:
    """Test the update API."""
    random_product["price"] = 100
    response = client.put(f"{settings.api.endpoint}/products/{random_product.get('id')}", json=random_product)
    assert response.ok


def test_delete_product(client: TestClient, random_product: Dict[str, Any]) -> None:
    """Test the delete API."""
    response = client.delete(f"{settings.api.endpoint}/products/{random_product.get('id')}")
    assert response.ok
