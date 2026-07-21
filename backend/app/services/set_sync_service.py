from sqlalchemy.orm import Session

from app.services.set_mapper import map_set_data
from app.services.set_service import get_or_create_set


def sync_set(
    db: Session,
    api_set_data: dict
):

    set_data = map_set_data(
        api_set_data
    )

    return get_or_create_set(
        db,
        set_data
    )