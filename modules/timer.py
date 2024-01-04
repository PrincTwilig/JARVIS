import time, logging, re
from notifications import answer
from helpers import isCommand

class Timer:
    def __init__(self):
        self.logger = logging.getLogger("Timer")

        self.time_words = {
            'один': ['один ', 'одна', 'одне', 'одні', 'одну'],
            'два': ['два', 'дві'],
            'три': ['три'],
            'чотири': ['чотири'],
            'п\'ять': ['п\'ять', 'пять'],
            'шість': ['шість'],
            'сім': ['сім'],
            'вісім': ['вісім'],
            'дев\'ять': ['дев\'ять', 'девять'],
            'десять': ['десять'],
            'одинадцять': ['одинадцять'],
            'дванадцять': ['дванадцять'],
            'тринадцять': ['тринадцять'],
            'чотирнадцять': ['чотирнадцять'],
            'п\'ятнадцять': ['п\'ятнадцять', 'пятнадцять'],
            'шістнадцять': ['шістнадцять'],
            'сімнадцять': ['сімнадцять'],
            'вісімнадцять': ['вісімнадцять'],
            'дев\'ятнадцять': ['дев\'ятнадцять', 'девятнадцять'],
            'двадцять': ['двадцять'],
        }

    def set_timer(self, text):
        seconds = self.get_time(text)

        self.logger.info(f"Таймер встановлено на {seconds} секунд")
        answer(f"Таймер встановлено на {seconds} секунд")

        self.timer(seconds)


    def timer(self, sleep):
        time.sleep(sleep)
        self.logger.info(f"Таймер {sleep} секунд закінчився!")
        answer(f"Таймер {sleep} секунд закінчився!")

    def get_time(self, text):
        text = text.lower().strip()

        seconds = 0
        minutes = 0
        hours = 0

        for i, time_word in enumerate(self.time_words.values()):
            for word in time_word:
                if word in text: # replace word with number as id in dict
                    text = text.replace(word, str(i+1))

        if re.search(r"(\d+) секунд", text):
            seconds = int(re.search(r"(\d+) секунд", text).group(1))

        if re.search(r"(\d+) хвилин", text):
            minutes = int(re.search(r"(\d+) хвилин", text).group(1))

        if re.search(r"(\d+) годин", text):
            hours = int(re.search(r"(\d+) годин", text).group(1))

        time_in_seconds = seconds + minutes * 60 + hours * 3600

        return time_in_seconds

    def analyze_text(self, text):
        text, is_command = isCommand(text, ["встанови таймер на", "встановити таймер на", "встанови таймер", "встановити таймер", "таймер"])

        if not is_command:
            return
        
        self.set_timer(text)
