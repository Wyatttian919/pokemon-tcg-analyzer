from app.core.database import SessionLocal
from app.api.pokemon_api import get_card_from_api
from app.services.set_service import get_or_create_set


db = SessionLocal()


card = get_card_from_api(
    "sv3-1"
)


pokemon_set = get_or_create_set(
    db,
    card["set"]
)


print(pokemon_set.id)
print(pokemon_set.name)