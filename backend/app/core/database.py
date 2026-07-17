from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..models.base import Base
from .. import models

DATABASE_URL = "sqlite:///pokemon.db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    bind=engine
)


def create_tables():
    Base.metadata.create_all(bind=engine)

