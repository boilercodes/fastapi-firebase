"""This is a generated example file that is supposed to be modified."""

from sqlalchemy import Column, Float, Integer, String

from app.db import Base


class Product(Base):
    """The product database table."""

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
