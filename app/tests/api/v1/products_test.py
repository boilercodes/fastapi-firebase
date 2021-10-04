"""This is a generated example file that is supposed to be modified."""

from typing import Any, Dict

import pytest
from fastapi.testclient import TestClient

from app.core import settings


@pytest.mark.skip()
def test_create_product(client: TestClient, random_product: Dict[str, Any]) -> None:
    """Test the create API."""
    response = client.post(f"{settings.API_ENDPOINT}/products", json=random_product)
    product = response.json()
    assert response.status_code == 200
    assert product.get("name") == random_product.get("name")
    assert product.get("price") == random_product.get("price")


@pytest.mark.skip()
def test_read_products(client: TestClient) -> None:
    """Test the read API."""
    response = client.get(f"{settings.API_ENDPOINT}/products")
    products = response.json()
    assert response.status_code == 200
    assert len(products) > 0


@pytest.mark.skip()
def test_update_product(client: TestClient, random_product: Dict[str, Any]) -> None:
    """Test the update API."""
    random_product["price"] = 100
    response = client.put(f"{settings.API_ENDPOINT}/products", json=random_product)
    product = response.json()
    assert response.status_code == 200
    assert product.get("price") == random_product.get("price")


@pytest.mark.skip()
def test_delete_product(client: TestClient, random_product: Dict[str, Any]) -> None:
    """Test the delete API."""
    response = client.delete(f"{settings.API_ENDPOINT}/products?id={random_product.get('id')}")
    message = response.json()
    assert response.status_code == 200
    assert "message" in message
