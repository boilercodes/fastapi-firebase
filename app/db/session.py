import logging
import sys
import time
from threading import Thread

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists

from app.core import settings
from app.db import Base
from app.utils.decorators import use_callbacks

log = logging.getLogger(__name__)


class Session(sessionmaker):
    """Represents a database session."""

    def __init__(self, use_sqlite: bool = False, **kw):
        # Add a background task to try to connect to the database.
        super().__init__(**kw)
        self.engine = None

        if use_sqlite:
            # Manually call the error callback to use sqlite.
            self.error_callback(BaseException("Using sqlite as stated."))
        else:
            thread = Thread(target=self.get_engine, args=(3, 1))
            thread.daemon = True
            thread.start()

    def callback(self, pg_dns: str) -> None:
        """Execute when the pool is completed."""
        log.info("Connection to the database successful.")

        self.engine = create_engine(pg_dns)
        self.kw["bind"] = self.engine

        Base.metadata.create_all(self.engine, checkfirst=True)

    def error_callback(self, error: BaseException) -> None:
        """Execute when the pool throws an error."""
        log.info(error)

        # Use sqlite if the connection to the database failed.
        self.engine = create_engine(settings.sqlite_dns)
        self.kw["bind"] = self.engine

        Base.metadata.create_all(self.engine, checkfirst=True)

    @use_callbacks
    def get_engine(self, timeout: int, delay: int) -> str:
        """Get an engine depending on the settings db."""
        for i in range(timeout):
            log.debug(f"Connecting to database {'.' * (timeout - i)}")
            if database_exists(settings.pg_dns):
                return settings.pg_dns
            time.sleep(delay)

        raise ConnectionError("Could not connect to the database, using sqlite.")


if "pytest" in sys.modules:
    settings.sqlite_dns = "sqlite:///pytest.sqlite3"  # Use pytest.sqlite3
    SessionLocal = Session(use_sqlite=True, autocommit=False, autoflush=False)
else:
    SessionLocal = Session(autocommit=False, autoflush=False)
