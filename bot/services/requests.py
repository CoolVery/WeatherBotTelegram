import requests_async as requests

from bot.config import BASE_URL, API_KEY

async def get_weather(city_name):
    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name
    
    response = await requests.get(complete_url)
    data = response.json()  # Преобразуем ответ в JSON
    print(data)
    return response
