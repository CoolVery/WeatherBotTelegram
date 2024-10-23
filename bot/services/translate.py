from translate import Translator

async def translate_name_city_to_en(city_name):
    translator = Translator(from_lang="ru", to_lang="en")
    en_city_name = translator.translate(city_name)
    return en_city_name