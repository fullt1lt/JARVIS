import sounddevice as sd
import threading
from queue import Queue
from vosk import Model, KaldiRecognizer

from source.settings import VOICE_MODEL


class VoiceRecognizer:
    def __init__(self):
        self.model = Model(VOICE_MODEL)
        self.queue_audio = Queue()
        self.queue_text = Queue()
        self.recognizer = KaldiRecognizer(self.model, 16000)
        self.__blocksize = 8000
        self.__samplerate = 16000
        self.__channels = 1
        self.__dtype = "int16"
        self.__running = True

    def _audio_callback(self, indata, frames, time, status):
        """Внутренний коллбек, пишет данные в очередь."""
        self.queue_audio.put(bytes(indata))

    def listen_command(self):
        with sd.RawInputStream(
            samplerate=self.__samplerate,
            blocksize=self.__blocksize,
            dtype=self.__dtype,
            channels=self.__channels,
            callback=self._audio_callback,
        ):
            print("🎙️ Начал слушать...")
            while True:
                data = self.queue_audio.get()
                if self.recognizer.AcceptWaveform(data):
                    result = self.recognizer.Result()
                    text = eval(result)["text"]
                    self.__stop_listening(text)
                    if self.__running and text:
                        print(f"Распознано: {text}")
                        self.queue_text.put(text)

    def start_listening(self):
        """Запускает прослушку в отдельном потоке."""
        thread = threading.Thread(target=self.listen_command)
        thread.daemon = True
        thread.start()



    def __stop_listening(self, command):
        """Остановить прослушку (например, перед когда не нужно выполнять команды)."""
        if command == "стоп":
            self.__running = False
            print("🛑 Остановили прослушивание")
        if command == "старт":
            self.__running = True
            print("Запуск прослушивания")
