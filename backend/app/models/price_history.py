from datetime import datetime
from decimal import Decimal

from sqlalchemy import ForeignKey, DateTime, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class PriceHistory(Base):

    __tablename__ = "price_histories"


    id: Mapped[int] = mapped_column(
        primary_key=True
    )


    card_id: Mapped[int] = mapped_column(
        ForeignKey("cards.id"),
        nullable=False
    )


    market_price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )


    recorded_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

