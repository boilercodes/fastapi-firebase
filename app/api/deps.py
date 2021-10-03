from typing import Generator

from app.db.session import SessionLocal


def get_db() -> Generator:
    """Returns a db instance."""
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
