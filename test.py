import os
from dotenv import load_dotenv
import requests

load_dotenv()
open_api_key=os.getenv("OPEN_AI_KEY")


def get_weather_by_city(city_name: str):
    base_url = f"https://wttr.in/{city_name}?format=%c+%t"
    response = requests.get(base_url)
    print(response.text)
    return response.text


