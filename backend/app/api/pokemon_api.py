import requests


BASE_URL = "https://api.pokemontcg.io/v2"


def get_card_from_api(card_id: str):

    print("CALL API:", card_id)

    url = f"{BASE_URL}/cards/{card_id}"

    try:

        response = requests.get(
            url,
            timeout=10
        )

        print("STATUS:", response.status_code)

        if response.status_code != 200:
            print("RESPONSE:", response.text[:300])

        response.raise_for_status()


    except requests.RequestException as e:

        print("ERROR:", e)

        return None


    data = response.json()

    return data["data"]