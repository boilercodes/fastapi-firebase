from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists

from app.core import settings
from app.db import Base

# Use sqlite if postgres doesn't work.
if database_exists(settings.pg_dns):
    engine = create_engine(settings.pg_dns)
else:
    engine = create_engine("sqlite:///db.sqlite3")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialise all tables and columns.
Base.metadata.create_all(engine, checkfirst=True)
