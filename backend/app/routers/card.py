from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.card import (
    CardCreate,
    CardUpdate,
    CardResponse
)

from app.services.card_service import (
    create_card,
    get_card,
    update_card,
    delete_card
)

router = APIRouter(
    prefix="/cards",
    tags=["Cards"]
)


@router.post(
    "/",
    response_model=CardResponse
)
def create_card_endpoint(
    card_data: CardCreate,
    db: Session = Depends(get_db)
):

    card = create_card(
        db,
        card_data
    )

    if card is None:
        raise HTTPException(
            status_code=400,
            detail="Card already exists"
        )

    return card


@router.get(
    "/{card_id}",
    response_model=CardResponse
)
def get_card_endpoint(
    card_id: int,
    db: Session = Depends(get_db)
):

    card = get_card(
        db,
        card_id
    )

    if card is None:
        raise HTTPException(
            status_code=404,
            detail="Card not found"
        )

    return card




@router.put(
    "/{card_id}",
    response_model=CardResponse
)
def update_card_endpoint(
    card_id: int,
    card_data: CardUpdate,
    db: Session = Depends(get_db)
):

    card = update_card(
        db,
        card_id,
        card_data
    )


    if card is None:
        raise HTTPException(
            status_code=404,
            detail="Card not found"
        )


    return card



@router.delete(
    "/{card_id}",
    response_model=CardResponse
)
def delete_card_endpoint(
    card_id: int,
    db: Session = Depends(get_db)
):

    card = delete_card(...)

    if card is None:
        raise HTTPException(
            status_code=404,
            detail="Card not found"
        )

    return card