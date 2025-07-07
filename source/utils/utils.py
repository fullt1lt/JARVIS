from datetime import datetime
import json
from num2words import num2words

from ..settings import COMMAND_FILE


def load_to_json():
    with open(COMMAND_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def convert_time_to_words() -> str:
    current_time = datetime.now().strftime("%H:%M")
    hours, minutes = map(int, current_time.split(":"))
    hours_word = num2words(hours, lang="ru")
    minutes_word = num2words(minutes, lang="ru")
    return f"{hours_word} {minutes_word}"

def hello_message():
    time_of_day = get_time_of_day()
    return f"{time_of_day}, СЭР. Чем могу помочь?"

def get_time_of_day():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 17:
        return "Добрый день"
    elif 17 <= hour < 22:
        return "Добрый вечер"
    else:
        return "Не спите"
