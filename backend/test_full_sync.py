from app.core.database import SessionLocal
from app.services.card_sync_service import sync_card


db = SessionLocal()


card = sync_card(
    db,
    "sv3-1"
)


print("RESULT:", card)
print(type(card))

if card:
    print(card.name)
    print(card.set.name)

    
db.close()