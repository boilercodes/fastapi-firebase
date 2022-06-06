"""This is a generated example file that is supposed to be modified."""

from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient

from app.__main__ import app
from app.firebase.session import db


@pytest.fixture(scope="session")
def get_db() -> Generator:
    """Return a database instance."""
    yield db


@pytest.fixture(scope="module")
def client() -> Generator:
    """Return the test client."""
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def random_product() -> Dict[str, str]:
    """Return a product example."""
    return {
        "name": "Test Product",
        "price": 80,
    }
