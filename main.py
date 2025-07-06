from source.voice_manager.voice_manager import VoiceRecognizer
from source.speaker_manager.speaker_manager import speak
from source.сommand_processing.command_processing import Comand_Processsing
import threading
import time

vr = VoiceRecognizer()
cm = Comand_Processsing()


def speaker_thread():
    while True:
        if not vr.queue_text.empty():
            command = vr.queue_text.get()
            print(f"🗣 Вы сказали: {command}")
            vr.ignore_input = True  # временно отключаем восприятие

            response = cm.get_command(command)
            if response:
                speak(response)

            vr.ignore_input = False
        time.sleep(0.1)


def main():
    vr.start_listening()
    speak_thread = threading.Thread(target=speaker_thread, daemon=True)
    speak_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("⛔ Завершаем")
        vr.stop_listening()


if __name__ == "__main__":
    main()
