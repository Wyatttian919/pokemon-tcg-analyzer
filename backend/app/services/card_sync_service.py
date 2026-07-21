from sqlalchemy.orm import Session

from app.api.pokemon_api import get_card_from_api

from app.services.set_sync_service import sync_set
from app.services.card_mapper import map_card_data
from app.services.card_service import create_card
from app.schemas.card import CardCreate


def sync_card(
    db: Session,
    api_card_id: str
):

    card_data = get_card_from_api(
        api_card_id
    )


    if card_data is None:
        raise ValueError(
            f"Cannot sync card: {api_card_id}"
        )


    pokemon_set = sync_set(
        db,
        card_data["set"]
    )


    mapped_card = map_card_data(
        card_data
    )


    mapped_card["set_id"] = pokemon_set.id


    card_create = CardCreate(
    **mapped_card
    )


    return create_card(
        db,
        card_create
    )