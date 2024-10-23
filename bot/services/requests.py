import requests_async as requests
from pprint import pprint
#import requests

from bot.config import BASE_URL, API_KEY

async def get_weather(city_name):
    complete_url = BASE_URL + "key=" + API_KEY + "&q=" + city_name
    try:
        response = await requests.get(complete_url, timeout=30)
        data = response.json()  # Преобразуем ответ в JSON
        return [requests.status_codes, data]
    except requests.ConnectionError as e:
        print(e)
        return None
    except requests.Timeout as e:
        print("Ошибка тайм-аута:", e)
        return None
    except requests.exceptions.HTTPError as e:
        print("Ошибка запроса:", e)
        return None
    except requests.exceptions.TooManyRedirects as e:
        print(e)
        return None
    except requests.RequestException as e:
        print(e)
        return None


