

async def json_to_message(json_answer):
    answer = f'Облачность в %: {json_answer["current"]["cloud"]}\n' \
            f'Градусы: {json_answer["current"]["temp_c"]}\n' \
            f'Влажность воздуха в %: {json_answer["current"]["humidity"]}\n' \
            f'Скорость ветра в км/ч: {json_answer["current"]["gust_kph"]}\n'
    return answer
