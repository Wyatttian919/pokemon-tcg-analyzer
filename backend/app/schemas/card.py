from typing import Optional

from pydantic import BaseModel

from app.schemas.pokemon_set import PokemonSetSimpleResponse


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



class CardSimpleResponse(BaseModel):

    id: int

    name: str

    number: str

    image_url: Optional[str] = None


    class Config:
        from_attributes = True


    
class CardSearchResponse(BaseModel):

    id: int

    name: str

    number: str

    rarity: Optional[str] = None

    image_url: Optional[str] = None


    class Config:
        from_attributes = True




class CardDetailResponse(BaseModel):

    id: int

    pokemon_api_id: str

    name: str

    number: str

    rarity: Optional[str] = None

    category: Optional[str] = None

    card_type: Optional[str] = None

    hp: Optional[int] = None

    image_url: Optional[str] = None

    set: PokemonSetSimpleResponse


    class Config:
        from_attributes = True