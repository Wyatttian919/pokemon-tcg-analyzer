from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import (
    Date,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    UniqueConstraint
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base



class CollectionItem(Base):
    
    __tablename__="collection_items"


    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "card_id",
            name="unique_user_card_collection"
        ),
    )


    id: Mapped[int] = mapped_column(
        primary_key=True
    )


    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )


    card_id: Mapped[int] = mapped_column(
        ForeignKey("cards.id"),
        nullable=False
    )


    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )


    condition: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )


    purchase_price: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2)
    )


    purchase_date: Mapped[date | None] = mapped_column(
        Date,
        default=date.today
    )


    acquisition_method: Mapped[str | None] = mapped_column(
        String(100)
    )


    notes: Mapped[str | None] = mapped_column(
        Text
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )


    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


    user = relationship(
        "User",
        back_populates="collection_items"
    )


    card = relationship(
        "Card",
        back_populates="collection_items"
    )