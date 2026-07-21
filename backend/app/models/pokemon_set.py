from datetime import date, datetime

from sqlalchemy import String, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class PokemonSet(Base):

    __tablename__ = "sets"


    id: Mapped[int] = mapped_column(
        primary_key=True
    )


    api_set_id: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )


    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )


    language: Mapped[str] = mapped_column(
            String(100),
            nullable=False,
            default="English"
    )


    series: Mapped[str | None] = mapped_column(
        String(100)
    )


    release_date: Mapped[date | None] = mapped_column(
        Date
    )


    logo_url: Mapped[str | None] = mapped_column(
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




