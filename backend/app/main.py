from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (
    card,
    user,
    collection_items,
    pokemon_set
)


app = FastAPI(
    title="Pokémon TCG Analyzer API",
    description="Backend API for Pokémon TCG collection management and analysis.",
    version="1.0.0"
)


# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=[
        "*"
    ],
    allow_headers=[
        "*"
    ],
)


app.include_router(user.router)
app.include_router(card.router)
app.include_router(collection_items.router)
app.include_router(pokemon_set.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Pokémon TCG Analyzer API"
    }