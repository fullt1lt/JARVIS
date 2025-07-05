import time
from source.voice_manager.voice_manager import VoiceRecognizer

vr = VoiceRecognizer()

def main():
    vr.start_listening()  # запускаем слушание в отдельном потоке

    try:
        while True:
            if not vr.queue_text.empty():
                command = vr.queue_text.get()
                print(f"🎧 Получена команда: {command}")

            time.sleep(0.2)
    except KeyboardInterrupt:
        print("⛔ Останавливаем...")
        vr.stop_listening()


if __name__ == "__main__":
    main()
