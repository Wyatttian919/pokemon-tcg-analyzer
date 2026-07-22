from app.api.pokemon_api import get_card_from_api


card = get_card_from_api(
    "sv3-1"
)

print(type(card))
print(card is None)

if card:
    print(card["name"])
# print(card["name"])
# print(card["set"]["name"])