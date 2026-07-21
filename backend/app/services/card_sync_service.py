from sqlalchemy.orm import Session

from app.models.card import Card
from app.models.pokemon_set import PokemonSet

from app.api.pokemon_api import get_card_from_api



def sync_card(
    db: Session,
    api_card_id: str
):

    card_data = get_card_from_api(api_card_id)


    if card_data is None:
        raise Exception("Card API returned None")


    return card_data