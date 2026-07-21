def map_card_data(card_data: dict):

    return {
        "pokemon_api_id": card_data["id"],

        "name": card_data["name"],

        "number": card_data["number"],

        "rarity": card_data.get("rarity"),

        "category": card_data.get("supertype"),

        "card_type": (
            card_data["types"][0]
            if card_data.get("types")
            else None
        ),

        "hp": (
            int(card_data["hp"])
            if card_data.get("hp")
            else None
        ),

        "image_url": (
            card_data["images"]["large"]
            if card_data.get("images")
            else None
        )
    }