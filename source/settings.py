import os

# Базовая директория 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Путь к голосовой модели
VOICE_MODEL = os.path.join(BASE_DIR, "models", "vosk-model-small-ru-0.22")
