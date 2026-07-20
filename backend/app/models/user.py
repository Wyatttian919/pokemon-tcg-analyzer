from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class User(Base):

    __tablename__ = "users"


    id: Mapped[int] = mapped_column(
        primary_key=True
    )


    username: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )


    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )


    password_hash: Mapped[str] = mapped_column(
        String(100),
        nullable=False
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


    collection_items = relationship(
        "CollectionItem",
        back_populates="user"
    )