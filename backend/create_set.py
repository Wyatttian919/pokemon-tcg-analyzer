from datetime import date

from app.core.database import SessionLocal
from app.models.pokemon_set import PokemonSet


db = SessionLocal()


test_set = PokemonSet(
    api_set_id="sv3pt5",
    name="Scarlet & Violet 151",
    language="English",
    series="Scarlet & Violet",
    release_date=date(2023, 9, 22),
    logo_url=None
)


db.add(test_set)

db.commit()

db.refresh(test_set)


print(test_set.id)


db.close()