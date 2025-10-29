import requests
from langchain.tools import tool

@tool
def get_weather(city: str):
    """Get the current weather of a given city."""
    base_url = f"https://wttr.in/{city}?format=%c+%t"
    response = requests.get(base_url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text.strip()}"
    return "Something went wrong while fetching the weather."