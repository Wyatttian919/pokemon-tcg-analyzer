from app.api.pokemon_api import get_card_from_api
from app.services.set_sync_service import sync_set
from app.core.database import SessionLocal


db = SessionLocal()


card = get_card_from_api(
    "sv3-1"
)


pokemon_set = sync_set(
    db,
    card["set"]
)


print(pokemon_set.id)
print(pokemon_set.name)
print(pokemon_set.language)


db.close()
