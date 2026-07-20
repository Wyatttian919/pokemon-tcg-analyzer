from sqlalchemy.orm import Session

from app.models.card import Card
from app.schemas.card import CardCreate, CardUpdate



def create_card(
    db: Session,
    card_data: CardCreate
):

    existing_card = db.query(Card).filter(
        Card.pokemon_api_id == card_data.pokemon_api_id
    ).first()


    if existing_card:
        return None


    card = Card(
        pokemon_api_id=card_data.pokemon_api_id,
        set_id=card_data.set_id,
        name=card_data.name,
        number=card_data.number,
        rarity=card_data.rarity,
        category=card_data.category,
        card_type=card_data.card_type,
        hp=card_data.hp,
        image_url=card_data.image_url
    )


    db.add(card)

    db.commit()

    db.refresh(card)

    return card



def get_card(
    db: Session,
    card_id: int
):

    return db.query(Card).filter(
        Card.id == card_id
    ).first()



def update_card(
    db: Session,
    card_id: int,
    card_data: CardUpdate
):

    card = db.query(Card).filter(
        Card.id == card_id
    ).first()


    if card is None:
        return None


    if card_data.name is not None:
        card.name = card_data.name


    if card_data.number is not None:
        card.number = card_data.number


    if card_data.rarity is not None:
        card.rarity = card_data.rarity


    if card_data.category is not None:
        card.category = card_data.category


    if card_data.card_type is not None:
        card.card_type = card_data.card_type


    if card_data.hp is not None:
        card.hp = card_data.hp


    if card_data.image_url is not None:
        card.image_url = card_data.image_url


    db.commit()

    db.refresh(card)

    return card



def delete_card(
    db: Session,
    card_id: int
):

    card = db.query(Card).filter(
        Card.id == card_id
    ).first()


    if card is None:
        return None


    db.delete(card)

    db.commit()

    return card