"""This is a generated example file that is supposed to be modified."""

from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from google.cloud import firestore

from app import schemas
from app.api.deps import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.ProductResponse])
def read_products(db: firestore.Client = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    """Retrieve all products."""
    ref = db.collection("products")
    docs = ref.limit(limit + skip).get()

    return [doc.to_dict() for doc in docs][skip:]


@router.post("", status_code=status.HTTP_201_CREATED, response_class=Response)
def create_product(*, db: firestore.Client = Depends(get_db), product_in: schemas.ProductCreate) -> Any:
    """Create new products."""
    ref = db.collection("products")
    ref.add(product_in.dict())


@router.get("/{product_id}", response_model=schemas.ProductResponse)
def read_product(*, db: firestore.Client = Depends(get_db), product_id: str) -> Any:
    """Read existing product."""
    ref = db.collection("products")
    doc = ref.document(product_id).get()
    if not doc.exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The product with this ID does not exist in the system.",
        )
    return doc.to_dict()


@router.put("/{product_id}", status_code=status.HTTP_200_OK, response_class=Response)
def update_product(*, db: firestore.Client = Depends(get_db), product_id: str,
                   product_in: schemas.ProductUpdate) -> Any:
    """Update existing products."""
    ref = db.collection("products")
    doc = ref.document(product_id).get()
    if not doc.exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The product with this ID does not exist in the system.",
        )
    doc.reference.update(product_in.dict())


@router.delete("/{product_id}", status_code=status.HTTP_200_OK, response_class=Response)
def delete_product(*, db: firestore.Client = Depends(get_db), product_id: str) -> Any:
    """Delete existing product."""
    ref = db.collection("products")
    doc = ref.document(product_id).get()
    if not doc.exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The product with this ID does not exist in the system.",
        )
    doc.reference.delete()
