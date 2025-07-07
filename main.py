from source.voice_manager.voice_manager import VoiceRecognizer
from source.сommand_processing.command_processing import Comand_Processsing
import threading
import time

from source.speaker_manager.speaker_manager import SileroSpeaker
from source.utils.utils import hello_message


vr = VoiceRecognizer()
cm = Comand_Processsing()
speaker = SileroSpeaker(speaker="aidar")

def speaker_thread():
    speaker.speak(hello_message())
    while True:
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
