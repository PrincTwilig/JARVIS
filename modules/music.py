import pytube, logging, time
from settings import temp_folder
import hashlib
import subprocess
from helpers import isCommand

class Music:
    def __init__(self) -> None:
        self.logger = logging.getLogger("Music")

        # turn off logging from pytube
        logging.getLogger("pytube").setLevel(logging.CRITICAL)
        self.current_song = None

    def turn_on_music(self, text: str) -> None:
        audio = self.get_audio(text)
        path = audio.download(temp_folder)

        subprocess.Popen(['start', '', path], shell=True)

    def get_audio(self, text: str) -> None:
        search = pytube.Search(text)
        video = search.results[0]
        audio_streams = video.streams.filter(only_audio=True)

        best_audio = max(audio_streams, key=lambda stream: int(
            stream.abr.replace("kbps", "")))
        return best_audio


    def analyze_text(self, text: str) -> None:
        text, is_command = isCommand(
            text, ['включи', 'включити', 'включає', 'відтвори', 'відтворити'])

        if not is_command:
            return

        self.turn_on_music(text)

        
        
        