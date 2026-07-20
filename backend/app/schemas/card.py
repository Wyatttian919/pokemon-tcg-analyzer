from typing import Optional

from pydantic import BaseModel


class CardCreate(BaseModel):

    pokemon_api_id: str

    set_id: int

    name: str

    number: str

    rarity: Optional[str] = None

    category: Optional[str] = None

    card_type: Optional[str] = None

    hp: Optional[int] = None

    image_url: Optional[str] = None



class CardUpdate(BaseModel):

    name: Optional[str] = None

    number: Optional[str] = None

    rarity: Optional[str] = None

    category: Optional[str] = None

    card_type: Optional[str] = None

    hp: Optional[int] = None

    image_url: Optional[str] = None



class CardResponse(BaseModel):

    id: int

    pokemon_api_id: str

    set_id: int

    name: str

    number: str

    rarity: Optional[str] = None

    category: Optional[str] = None

    card_type: Optional[str] = None

    hp: Optional[int] = None

    image_url: Optional[str] = None


    class Config:
        from_attributes = True