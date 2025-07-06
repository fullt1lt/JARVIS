import json
import random
import subprocess

from ..settings import COMMAND_FILE, PROGRAMS

def load_to_json():
    with open(COMMAND_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


class Comand_Processsing:
    def __init__(self):
        self.commands = load_to_json()
        self.__name_command = "джарвис"

    def __prepare_command(self, voice_text: str):
        voice_text = voice_text.lower()
        if self.__name_command in voice_text:
            return voice_text.replace(self.__name_command, "").strip()

    def get_command(self, voice_text: str):
        prepared_text = self.__prepare_command(voice_text)
        if not prepared_text:
            return None
        return self.choose_command(prepared_text)

    def choose_command(self, prepared_text: str):
        response = None
        for key, value in self.commands.items():
            if prepared_text.startswith(key.lower()):
                if value['type'] == 'text':
                    response = random.choice(value.get("response", [""]))
                    print(f"Команда найдена: {key} -> {response}") #!!!!!!!
                    return response

                elif value['type'] == 'action':
                    response = random.choice(value.get("response", [""]))
                    self.run_program(value["action"])
                    return response
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

