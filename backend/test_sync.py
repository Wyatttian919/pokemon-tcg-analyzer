from app.services.card_sync_service import sync_card
from app.core.database import SessionLocal


db = SessionLocal()


card = sync_card(
    db,
    "sv3-1"
)


print(card["name"])
print(card["set"]["name"])