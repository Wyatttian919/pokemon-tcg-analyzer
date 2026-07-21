from app.api.pokemon_api import get_card_from_api
from app.services.set_mapper import map_set_data


card = get_card_from_api(
    "sv3-1"
)


set_data = card["set"]


mapped_set = map_set_data(
    set_data
)


print(mapped_set)