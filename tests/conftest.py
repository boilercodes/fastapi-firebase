"""This is a generated example file that is supposed to be modified."""

from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient

from app.__main__ import app
from app.db.session import SessionLocal


@pytest.fixture(scope="session")
def db() -> Generator:
    """Return a database instance."""
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    """Return the test client."""
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def random_product() -> Dict[str, str]:
    """Return a product example."""
    return {
        "id": 1,
        "name": "Test Product",
        "price": 80,
    }
