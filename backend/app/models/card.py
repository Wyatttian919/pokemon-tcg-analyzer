from datetime import datetime

from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Card(Base):

    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    pokemon_api_id: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    set_id: Mapped[int] = mapped_column(
        ForeignKey("sets.id"),
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    number: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    rarity: Mapped[str | None] = mapped_column(
        String(50)
    )

    category: Mapped[str | None] = mapped_column(
        String(50)
    )

    card_type: Mapped[str | None] = mapped_column(
        String(50)
    )

    hp: Mapped[int | None] = mapped_column(
        Integer
    )

    image_url: Mapped[str | None] = mapped_column(
        String(255)
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