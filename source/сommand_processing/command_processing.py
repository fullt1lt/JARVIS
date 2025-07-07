import random
import subprocess

from ..settings import  PROGRAMS, NAME_VOICE_ASSISTANT
from ..utils.utils import load_to_json, convert_time_to_words


class Comand_Processsing:
    def __init__(self, app_manager: "AppManager"):
        self.commands = load_to_json()
        self.__name_command = NAME_VOICE_ASSISTANT
        self.app_manager = app_manager

    def __prepare_command(self, voice_text: str):
        voice_text = voice_text.lower()
        if self.__name_command in voice_text:
            return voice_text.replace(self.__name_command, "").strip()
        return None

    def get_command(self, voice_text: str):
        prepared_text = self.__prepare_command(voice_text)
        if prepared_text is None:
            return None
        return self.choose_command(prepared_text)

    def choose_command(self, prepared_text: str):
        if self.__is_empty_command(prepared_text): # Проверка на пустую команду
            return self._handle_empty_command()
        for key, value in self.commands.items():
            if key == "":
                continue
            if prepared_text.startswith(key.lower()):
                if value['type'] == 'text':
                    response = random.choice(value.get("response", [""]))
                    print(f"Команда найдена: {key} -> {response}") #!!!!!!!
                    return response

                elif value['type'] == 'action':
                    response = random.choice(value.get("response", [""]))
                    action_name = value.get("action")
                    program_name = value.get("program_name")
                    if action_name.startswith("close"):
                        self.app_manager.close_program(program_name)
                    else:
                        self.app_manager.run_program(program_name)
                    return response
                elif value['type'] == 'data_text':
                    time_in_words = convert_time_to_words()
                    response_options = [
                        f"Сейчас {time_in_words}",
                        f"Время: {time_in_words}",
                        f"На часах: {time_in_words}"
                    ]
                    return random.choice(response_options)
                else:
                    print(f"Неизвестный тип команды: {value['type']}")
                    return "Команда найдена, но тип неизвестен."
        print(f"🔍 Команда не распознана: {prepared_text}")
        return "Извините, я не понял команду."

    def __is_empty_command(self, prepared_text: str):
        """Проверка, является ли команда пустой (т.е. пользователь просто говорит имя ассистента)."""
        return prepared_text == "" and "" in self.commands

    def _handle_empty_command(self) -> str:
        """Обработка пустой команды, когда пользователь просто говорит имя ассистента."""
        value = self.commands[""]
        if value["type"] == "text":
            return random.choice(value.get("response", [""]))
        else:
            return "Команда не может быть выполнена."
