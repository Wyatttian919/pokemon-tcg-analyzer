from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..models.base import Base
from .. import models

DATABASE_URL = "sqlite:///pokemon.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
