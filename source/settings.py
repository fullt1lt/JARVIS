import os

# Базовая директория
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMMAND_FILE = os.path.join(BASE_DIR, "commands", "commands.json")

# Путь к голосовой модели
VOICE_MODEL = os.path.join(BASE_DIR, "models", "vosk-model-small-ru-0.22")

NAME_VOICE_ASSISTANT = "джарвис"  # Имя голосового ассистента

# Пути к программам на компьютере
PROGRAMS = {
    "chrome": r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "vscode": r"C:\\Users\\Даниил\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
}
