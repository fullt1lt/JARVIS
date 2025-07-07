import torch
import sounddevice as sd
import time


class SileroSpeaker:

    def __init__(
        self, speaker: str = "aidar", sample_rate: int = 48000, device: str = "cpu"
    ):
        self.language = "ru"
        self.model_id = "ru_v3"
        self.sample_rate = sample_rate
        self.speaker = speaker
        self.put_accent = True
        self.put_yo = True
        self.device = torch.device(device)

        print("🔊 Загружаю модель Silero TTS...")
        self.model, _ = torch.hub.load(
            repo_or_dir="snakers4/silero-models",
            model="silero_tts",
            language=self.language,
            speaker=self.model_id,
        )
        self.model.to(self.device)

    def speak(self, text: str):
        try:
            audio = self.model.apply_tts(
                text=text + "...",
                speaker=self.speaker,
                sample_rate=self.sample_rate,
                put_accent=self.put_accent,
                put_yo=self.put_yo,
            )

            sd.play(audio, self.sample_rate * 1.05)
            time.sleep(len(audio) / self.sample_rate * 1.05 + 0.3)
            sd.stop()
        except Exception as e:
            print(f"[Ошибка Silero TTS]: {e}")
