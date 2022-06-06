from typing import Generator

from app.firebase.session import db


def get_db() -> Generator:
    """Returns a db instance."""
    yield db
