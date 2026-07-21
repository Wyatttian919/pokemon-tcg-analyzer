from sqlalchemy.orm import Session
# from fastapi import HTTPException

from app.models.collection_item import CollectionItem
from app.models.user import User
from app.models.card import Card

from app.schemas.collection_item import (
    CollectionItemCreate,
    CollectionItemUpdate
)



def create_collection_item(
    db: Session,
    item_data: CollectionItemCreate
):
       
    user = db.query(User).filter(
        User.id == item_data.user_id
    ).first()


    if user is None:
        return None


    card = db.query(Card).filter(
        Card.id == item_data.card_id
    ).first()


    if card is None:
        return None


    existing_item = db.query(CollectionItem).filter(
            CollectionItem.user_id == item_data.user_id,
            CollectionItem.card_id == item_data.card_id
        ).first()


    if existing_item:
        existing_item.quantity += item_data.quantity

        if item_data.purchase_price is not None:
            existing_item.purchase_price = item_data.purchase_price

        if item_data.condition is not None:
            existing_item.condition = item_data.condition


        db.commit()

        db.refresh(existing_item)

        return existing_item
    
    item = CollectionItem(
        user_id=item_data.user_id,
        card_id=item_data.card_id,
        quantity=item_data.quantity, 
        condition=item_data.condition,
        purchase_price=item_data.purchase_price,
        purchase_date=item_data.purchase_date,
        acquisition_method=item_data.acquisition_method,
        notes=item_data.notes
    )


    db.add(item)

    db.commit()

    db.refresh(item)


    return item



def get_collection_item(
    db: Session,
    item_id: int
):

    return db.query(CollectionItem).filter(
        CollectionItem.id == item_id
    ).first()



def update_collection_item(
    db: Session,
    item_id: int,
    item_data: CollectionItemUpdate
):

    item = db.query(CollectionItem).filter(
        CollectionItem.id == item_id
    ).first()


    if item is None:
        # raise HTTPException(
        #     status_code=400,
        #     detail="Collection item already exists or invalid user/card"
        # )
        return None

    if item_data.quantity is not None:
        item.quantity = item_data.quantity


    if item_data.condition is not None:
        item.condition = item_data.condition


    if item_data.purchase_price is not None:
        item.purchase_price = item_data.purchase_price


    if item_data.purchase_date is not None:
        item.purchase_date = item_data.purchase_date


    if item_data.acquisition_method is not None:
        item.acquisition_method = item_data.acquisition_method


    if item_data.notes is not None:
        item.notes = item_data.notes


    db.commit()

    db.refresh(item)

    return item



def delete_collection_item(
    db: Session,
    item_id: int
):

    item = db.query(CollectionItem).filter(
        CollectionItem.id == item_id
    ).first()


    if item is None:
        return None


    db.delete(item)

    db.commit()


    return item



def get_user_collection(
    db: Session,
    user_id: int
):

    return db.query(CollectionItem).filter(
        CollectionItem.user_id == user_id
    ).all()