from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.set_service import (
    get_set,
    get_set_cards
)

from app.schemas.pokemon_set import PokemonSetResponse
from app.schemas.card import CardSimpleResponse


router = APIRouter(
    prefix="/sets",
    tags=["Sets"]
)


@router.get(
    "/{set_id}",
    response_model=PokemonSetResponse
)
def get_set_endpoint(
    set_id:int,
    db:Session=Depends(get_db)
):

    pokemon_set = get_set(
        db,
        set_id
    )

    if pokemon_set is None:
        raise HTTPException(
            status_code=404,
            detail="Set not found"
        )

    return pokemon_set



@router.get(
    "/{set_id}/cards",
    response_model=list[CardSimpleResponse]
)
def get_set_cards_endpoint(
    set_id:int,
    db:Session=Depends(get_db)
):

    cards = get_set_cards(
        db,
        set_id
    )

    if cards is None:
        raise HTTPException(
            status_code=404,
            detail="Set not found"
        )

    return cards