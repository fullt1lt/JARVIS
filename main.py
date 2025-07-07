from source.voice_manager.voice_manager import VoiceRecognizer
from source.сommand_processing.command_processing import Comand_Processsing
import threading
import time

from source.speaker_manager.speaker_manager import SileroSpeaker
from source.utils.utils import hello_message
from source.utils.app_manager import AppManager


vr = VoiceRecognizer()
cm = Comand_Processsing(AppManager())
speaker = SileroSpeaker(speaker="aidar")
app_running = True 


def speaker_thread():
    speaker.speak(hello_message())
    while app_running:
        if not vr.queue_text.empty():
            command = vr.queue_text.get()
            print(f"🗣 Вы сказали: {command}")
            vr.ignore_input = True  # временно отключаем восприятие

            response = cm.get_command(command)
            if response:
                speaker.speak(response)

            vr.ignore_input = False
        time.sleep(0.1)


def main():
    global app_running

    vr.start_listening()
    speak_thread = threading.Thread(target=speaker_thread, daemon=True)
    speak_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("⛔ Завершаем")
        app_running = False  # сигнал на выход speaker-потоку
        vr.terminate()  # полная остановка прослушки
        speak_thread.join(timeout=2)
        print("✅ Всё остановлено корректно.")


if __name__ == "__main__":
    main()
