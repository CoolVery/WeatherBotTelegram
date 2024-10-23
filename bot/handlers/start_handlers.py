from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from bot.services.translate import translate_name_city_to_en
from bot.services.requests import get_weather
from bot.services.generate_answer import json_to_message

from pprint import pprint


router = Router()

class SearchCity(StatesGroup):
    city = State()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Здравствуй, {message.from_user.full_name}\n'
                         f'Вот весь мой функционал:\n' 
                         f'1. /city_weather - погода по городу')
    
@router.message(Command('city_weather'))
async def get_city_name(message: Message, state: FSMContext):
    await state.set_state(SearchCity.city)
    await message.answer('Введите название города, погоду которого вы хотите узнать')

@router.message(SearchCity.city)
async def get_city_weather(message: Message, state: FSMContext):
    await state.update_data(city = message.text)
    date = await state.get_data()
    await state.clear()
    en_city_name = await translate_name_city_to_en(date["city"])
    json_answer = await get_weather(en_city_name)
    if (json_answer[0] == 400):
            await message.answer("Введите правильное название города") 
    else:
        answer_str = await json_to_message(json_answer[1])
        await message.answer(answer_str) 
