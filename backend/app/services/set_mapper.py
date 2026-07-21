from datetime import datetime


def map_set_data(set_data: dict):

    release_date = None

    if set_data.get("releaseDate"):
        release_date = datetime.strptime(
            set_data["releaseDate"],
            "%Y/%m/%d"
        ).date()


    return {
        "api_set_id": set_data["id"],

        "name": set_data["name"],

        "series": set_data.get("series"),

        "language": "English",

        "release_date": release_date,

        "logo_url": (
            set_data["images"]["logo"]
            if set_data.get("images")
            else None
        )
    }