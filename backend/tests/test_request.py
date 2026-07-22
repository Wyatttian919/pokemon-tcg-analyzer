import requests


url = "https://api.pokemontcg.io/v2/cards/sv3-1"


response = requests.get(
    url,
    timeout=10
)


print(response.status_code)
print(response.text[:500])