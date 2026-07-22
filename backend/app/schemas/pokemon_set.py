from typing import Optional
from datetime import date

from pydantic import BaseModel



class PokemonSetCreate(BaseModel):

    api_set_id: str

    name: str

    language: str = "English"

    series: Optional[str] = None

    release_date: Optional[date] = None

    logo_url: Optional[str] = None



class PokemonSetResponse(BaseModel):

    id: int

    api_set_id: str

    name: str

    language: str

    series: Optional[str] = None

    release_date: Optional[date] = None

    logo_url: Optional[str] = None


    class Config:
        from_attributes = True



class PokemonSetSimpleResponse(BaseModel):

    id: int

    api_set_id: str

    name: str

    language: str


    class Config:
        from_attributes = True