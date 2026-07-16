from fastapi import APIRouter

router = APIRouter(
    prefix="/cards",
    tags=["Cards"]
)


@router.get("/")
def get_cards():
    return {
        "message" : "Card search endpoint"
    }

@router.get("/{card_id}")
def get_card(card_id:str):
    return {
        "card_id": card_id,
        "message": "Card detail endpoint"
    }