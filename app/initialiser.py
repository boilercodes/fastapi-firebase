from app.db import initialise
from app.db.session import SessionLocal


def init() -> None:
    """Run database initialisation queries."""
    db = SessionLocal()
    initialise(db)


if __name__ == "__main__":
    init()
