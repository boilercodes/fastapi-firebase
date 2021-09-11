"""This is a generated example file that is supposed to be modified."""

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api.deps import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.ProductResponse])
def read_products(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """Retrieve all products."""
    products = crud.product.get_multi(db, skip=skip, limit=limit)
    return products


@router.post("", status_code=status.HTTP_201_CREATED, response_class=Response)
def create_product(*, db: Session = Depends(get_db), product_in: schemas.ProductCreate) -> Any:
    """Create new products."""
    crud.product.create(db, obj_in=product_in)


@router.get("/{product_id}", response_model=schemas.ProductResponse)
def read_product(*, db: Session = Depends(get_db), product_id: int) -> Any:
    """Delete existing product."""
    product = crud.product.get(db, model_id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The product with this ID does not exist in the system.",
        )
    return product


@router.put("/{product_id}", status_code=status.HTTP_200_OK, response_class=Response)
def update_product(*, db: Session = Depends(get_db), product_id: int, product_in: schemas.ProductUpdate) -> Any:
    """Update existing products."""
    product = crud.product.get(db, model_id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The product with this ID does not exist in the system.",
        )
    crud.product.update(db, db_obj=product, obj_in=product_in)


@router.delete("/{product_id}", status_code=status.HTTP_200_OK, response_class=Response)
def delete_product(*, db: Session = Depends(get_db), product_id: int) -> Any:
    """Delete existing product."""
    product = crud.product.get(db, model_id=product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The product with this ID does not exist in the system.",
        )
    crud.product.remove(db, model_id=product_id)
