import time
import threading

from ..utils.utils import hello_message


class MainThread:
    def __init__(self, vr, cp, speaker, app_manager):
        self.vr = vr
        self.cm = cp
        self.speaker = speaker
        self.app_manager = app_manager
        self.app_running = True

    def speaker_thread(self):
        while self.app_running:
            if not self.vr.queue_text.empty():
                command = self.vr.queue_text.get()
                print(f"🗣 Вы сказали: {command}")
                self.vr.ignore_input = True  # временно отключаем восприятие
                response = self.cm.get_command(command)
                if response:
                    self.speaker.speak(response)    
                self.vr.ignore_input = False
            time.sleep(0.1)

    def start(self):
        self.speaker.speak(hello_message())
        self.vr.start_listening()
        self.speak_thread = threading.Thread(target=self.speaker_thread, daemon=True)
        self.speak_thread.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Завершаем")
            self.app_running = False
            self.vr.terminate()
            self.speak_thread.join(timeout=2)
            print("Всё остановлено корректно.")
