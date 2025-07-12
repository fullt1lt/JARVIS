import time
import threading
from PyQt5.QtCore import QTimer
from source.utils.utils import hello_message


class MainThread:
    def __init__(self, vr, cp, speaker, app_manager, gui):
        self.vr = vr
        self.cm = cp
        self.speaker = speaker
        self.app_manager = app_manager
        self.gui = gui
        self.app_running = True

    def speaker_thread(self):
        while self.app_running:
            if not self.vr.queue_text.empty():
                command = self.vr.queue_text.get()
                print(f"🗣 Вы сказали: {command}")
                self.vr.ignore_input = True

                response = self.cm.get_command(command)

                if response:
                    self.gui.start_speaking_animation()
                    self.speaker.speak(response)
                    self.gui.stop_speaking_animation()

                # Возвращаем в режим прослушки с задержкой (опционально)
                QTimer.singleShot(300, self.gui.set_listening_status)

                self.vr.ignore_input = False
            time.sleep(0.1)

    def start(self):
        self.vr.start_listening()
        self.gui.set_listening_status()
        self.speaker.speak(hello_message())

        self.speak_thread = threading.Thread(target=self.speaker_thread, daemon=True)
        self.speak_thread.start()
