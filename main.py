from source.voice_manager.voice_manager import VoiceRecognizer
from source.сommand_processing.command_processing import Comand_Processsing
from source.speaker_manager.speaker_manager import SileroSpeaker
from source.utils.app_manager import AppManager
from source.main_thread.main_thread import MainThread

def main():
    vr = VoiceRecognizer()
    cp = Comand_Processsing(AppManager())
    speaker = SileroSpeaker(speaker="aidar")
    ap = AppManager()
    main_thread = MainThread(vr, cp, speaker, ap)
    main_thread.start()
    
if __name__ == "__main__":
    main()