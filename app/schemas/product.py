"""This is a generated example file that is supposed to be modified."""

from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    """The base product model."""

    id: Optional[int]
    name: Optional[str]
    price: Optional[float]


class ProductCreate(BaseModel):
    """POST request product model."""

    name: str
    price: float


class ProductUpdate(BaseModel):
    """PUT request product model."""

    name: Optional[str]
    price: Optional[float]


class ProductResponse(ProductBase):
    """GET request product model."""

    class Config:
        """The Pydantic configuration class."""

        orm_mode = True
