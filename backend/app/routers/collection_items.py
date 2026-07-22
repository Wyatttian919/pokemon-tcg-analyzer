from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.collection_item import (
    CollectionItemCreate,
    CollectionItemResponse,
    CollectionItemUpdate
)

from app.services.collection_item_service import (
    get_collection_item,
    create_collection_item,
    update_collection_item,
    delete_collection_item
)

router = APIRouter(
    prefix="/collection-items",
    tags=["Collection Items"]
)



@router.post(
    "/",
    response_model=CollectionItemResponse
)
def create_collection_item_endpoint(
    item_data: CollectionItemCreate,
    db: Session = Depends(get_db)
):
    
    item = create_collection_item(
        db,
        item_data
    )

    if item is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid user or card"
        )

    return item



@router.get(
    "/{item_id}",
    response_model=CollectionItemResponse
)
def get_collection_item_endpoint(
    item_id: int,
    db: Session = Depends(get_db)
):

    item = get_collection_item(
        db,
        item_id
    )

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Collection item not found"
        )

    return item



@router.put(
    "/{item_id}",
    response_model=CollectionItemResponse
)
def update_collection_item_endpoint(
    item_id: int,
    item_data: CollectionItemUpdate,
    db: Session = Depends(get_db)
):

    item = update_collection_item(
        db,
        item_id,
        item_data
    )


    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Collection item not found"
        )


    return item



@router.delete(
    "/{item_id}",
    response_model=CollectionItemResponse
)
def delete_collection_item_endpoint(
    item_id: int,
    db: Session = Depends(get_db)
):

    item = delete_collection_item(
        db,
        item_id
    )

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Collection item not found"
        )

    return item



