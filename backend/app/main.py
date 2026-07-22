from fastapi import FastAPI
from app.routers import card, user, collection_items, pokemon_set

app = FastAPI(
    title="Pokémon TCG Analyzer API",
    description="Backend API for Pokémon TCG collection management and analysis.",
    version="1.0.0"
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