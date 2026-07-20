from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate



def create_user(
    db: Session,
    user_data: UserCreate
):
    

    existing_user = db.query(User).filter(
        User.username == user_data.username
    ).first()


    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )
    
    user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=user_data.password
    )



    db.add(user)

    db.commit()

    db.refresh(user)


    return user


def get_user(
    db: Session,
    user_id: int
):
    user = db.query(User).filter(
        User.id == user_id
    ).first()


    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


    return user



def update_user(
        db: Session,
        user_id: int,
        user_data: UserUpdate
):
    
    user = db.query(User).filter(
        User.id == user_id
    ).first()


    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    

    if user_data.username is not None:
        user.username = user_data.username

    
    if user_data.email is not None:
        user.email = user_data.email

    
    db.commit()

    db.refresh(user)

    return user



def delete_user(
    db: Session,
    user_id: int
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()


    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


    db.delete(user)

    db.commit()

    return user