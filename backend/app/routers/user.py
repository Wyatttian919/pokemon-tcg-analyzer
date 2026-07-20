from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal, get_db
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import (
    create_user,
    get_user,
    update_user,
    delete_user
)


router = APIRouter(
    prefix="/users",
    tags=["users"]
)




@router.post(
    "/",
    response_model=UserResponse
)
def create_user_endpoint(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    
    return create_user(
        db,
        user
    )


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def read_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    return get_user(
        db,
        user_id
    )


@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user_endpoint(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):

    return update_user(
        db,
        user_id,
        user_data
    )


@router.delete(
    "/{user_id}",
    response_model=UserResponse
)
def delete_user_endpoint(
    user_id: int,
    db: Session = Depends(get_db)
):

    return delete_user(
        db,
        user_id
    )