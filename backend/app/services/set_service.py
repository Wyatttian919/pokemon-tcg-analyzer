from sqlalchemy.orm import Session

from app.models.pokemon_set import PokemonSet



def get_or_create_set(
    db: Session,
    set_data: dict
):

    api_set_id = set_data["api_set_id"]


    existing_set = db.query(PokemonSet).filter(
        PokemonSet.api_set_id == api_set_id
    ).first()


    if existing_set:
        return existing_set


    new_set = PokemonSet(
        api_set_id=set_data["api_set_id"],
        name=set_data["name"],
        series=set_data.get("series"),
        release_date=set_data.get("release_date"),
        logo_url=set_data.get("logo_url"),
        language=set_data.get("language")
    )


    db.add(new_set)

    db.commit()

    db.refresh(new_set)


    return new_set



def get_set(
    db: Session,
    set_id: int
):

    return db.query(PokemonSet).filter(
        PokemonSet.id == set_id
    ).first()



def get_set_cards(
    db: Session,
    set_id: int
):

    pokemon_set = db.query(PokemonSet).filter(
        PokemonSet.id == set_id
    ).first()

    if pokemon_set is None:
        return None

    return pokemon_set.cards