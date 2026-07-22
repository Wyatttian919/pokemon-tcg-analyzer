from app.api.pokemon_api import get_card_from_api
from app.services.card_mapper import map_card_data


card = get_card_from_api(
    "sv3-1"
)


mapped_card = map_card_data(
    card
)


print(mapped_card)