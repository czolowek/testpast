import os

import requests
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv("WEATHER_API")


def get_weather(city: str = "Odesa"):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    resp = requests.get(url).json()

    current_weather = {
        "city": city,
        "temp": resp.get("current", {}).get("temp_c", "Дані з сайту не отримано"),
        "text": resp.get("current", {}).get("condition", {}).get("text"),
        "icon": resp.get("current", {}).get("condition", {}).get("icon")
    }

    return current_weather
