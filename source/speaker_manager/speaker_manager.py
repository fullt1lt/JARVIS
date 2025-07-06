from gtts import gTTS
from playsound import playsound
import tempfile
import os
import uuid


def speak(text, lang="ru"):
    try:
        temp_dir = tempfile.gettempdir()
        filename = os.path.join(temp_dir, f"{uuid.uuid4()}.mp3")
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print(f"[Ошибка озвучки]: {e}")
