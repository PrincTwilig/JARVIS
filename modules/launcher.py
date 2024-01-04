import subprocess
import logging
from helpers import isCommand


class Launcher:
    def __init__(self):
        self.logger = logging.getLogger("Launcher")

        self.program_keywords = {
            "chrome": ["хром", "хроміум", "chrome", "chromium"],
            "discord": ["дискорд", "discord"],
            "telegram": ["телеграм", "telegram"],
            "steam": ["стім", "steam"],
            "spotify": ["спотіфай", "spotify"],
            "minecraft": ["майнкрафт", "minecraft"]
        }

        self.program_paths = {
            "chrome": r"C:\Users\vladm\AppData\Local\Google\Chrome\Application\chrome.exe",
            "discord": r"C:\Users\vladm\AppData\Local\Discord\app-1.0.9028\Discord.exe",
            "telegram": r"C:\Users\vladm\AppData\Roaming\Telegram Desktop\Telegram.exe",
            "steam": r"D:\Steam\steam.exe",
            "spotify": r"C:\Users\vladm\AppData\Roaming\Spotify\Spotify.exe",
            "minecraft": r"C:\Users\vladm\AppData\Roaming\.minecraft\TLauncher.exe"
        }

    def launch_program(self, text):
        program = self.get_program(text)

        if not program:
            return

        self.logger.info(f"Запускаємо програму: {program}")

        subprocess.Popen(
            ['start', '', self.program_paths[program]], shell=True)

    def get_program(self, text):
        for program, keywords in self.program_keywords.items():
            for keyword in keywords:
                if keyword in text:
                    return program

    def analyze_text(self, text):
        text, is_command = isCommand(text, ["запусти", "запустити"])

        if not is_command:
            return

        self.launch_program(text)
