"""This is a generated example file that is supposed to be modified."""

from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    id: Optional[int]
    name: Optional[str]
    price: Optional[float]


class ProductCreate(BaseModel):
    name: str
    price: float


class ProductUpdate(BaseModel):
    name: Optional[str]
    price: Optional[float]


class ProductResponse(ProductBase):
    class Config:
        orm_mode = True
