from decimal import Decimal
from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel
from app.schemas.card import CardSimpleResponse
from app.schemas.user import UserSimpleResponse

class CollectionItemCreate(BaseModel):

    user_id: int

    card_id: int

    quantity: int

    condition: str

    purchase_price: Optional[Decimal] = None

    purchase_date: Optional[date] = None

    acquisition_method: Optional[str] = None

    notes: Optional[str] = None



class CollectionItemUpdate(BaseModel):

    quantity: Optional[int] = None

    condition: Optional[str] = None

    purchase_price: Optional[Decimal] = None

    purchase_date: Optional[date] = None

    acquisition_method: Optional[str] = None

    notes: Optional[str] = None



class CollectionItemResponse(BaseModel):

    id: int

    quantity: int

    condition: str


    card: CardSimpleResponse

    user: UserSimpleResponse


    class Config:
        from_attributes = True



class CollectionItemListResponse(BaseModel):

    id: int

    quantity: int

    condition: str

    purchase_price: Decimal | None

    card: CardSimpleResponse


    class Config:
        from_attributes = True