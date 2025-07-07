import random
import subprocess

from ..settings import  PROGRAMS, NAME_VOICE_ASSISTANT
from ..utils.utils import load_to_json, convert_time_to_words


class Comand_Processsing:
    def __init__(self):
        self.commands = load_to_json()
        self.__name_command = NAME_VOICE_ASSISTANT

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
                    self.run_program(value["action"])
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
                    print(f"❌ Неизвестный тип команды: {value['type']}")
                    return "Команда найдена, но тип неизвестен."
        print(f"🔍 Команда не распознана: {prepared_text}")
        return "Извините, я не понял команду."

    def run_program(self, program_name: str):
        if program_name in PROGRAMS:
            program_path = PROGRAMS[program_name]
            try:
                subprocess.Popen(program_path)
                # ДЛя откладки
                print( f"Запускаю {program_name}")
            except Exception as e:
                # ДЛя откладки
                print(f"Не удалось запустить программу {program_name}: {str(e)}")
        else:
            # ДЛя откладки
            print(f"Программа {program_name} не найдена в настройках.")

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
