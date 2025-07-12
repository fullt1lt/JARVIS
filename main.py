import sys
import threading
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from source.voice_manager.voice_manager import VoiceRecognizer
from source.сommand_processing.command_processing import Comand_Processsing
from source.speaker_manager.speaker_manager import SileroSpeaker
from source.utils.app_manager import AppManager
from source.main_thread.main_thread import MainThread
from source.gui.gui_voice_assistans import CustomWindow


def initialize_assistant_async(gui):
    QTimer.singleShot(
        0, lambda: gui.update_status("🛠️ Загружается голосовой ассистент...")
    )

    # Выполняем инициализацию
    vr = VoiceRecognizer() 
    cp = Comand_Processsing(AppManager())
    speaker = SileroSpeaker(speaker="aidar")
    ap = AppManager()

    main_thread = MainThread(vr, cp, speaker, ap, gui)

    # Запускаем main_thread из GUI-потока
    QTimer.singleShot(0, main_thread.start())


def main():
    app = QApplication(sys.argv)
    gui = CustomWindow()
    gui.show()

    threading.Thread(
        target=initialize_assistant_async, args=(gui,), daemon=True
    ).start()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
