from sqlalchemy.orm import Session

from app.models.card import Card


def search_cards(
    db: Session,
    name: str
):

    return db.query(Card).filter(
        Card.name.ilike(f"%{name}%")
    ).all()