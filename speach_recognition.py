import speech_recognition as sr
import logging
import time
import datetime
import threading
import os
import json
from models import voice_recognition_model
from modules import modules
from settings import full_path_to_vosk_model

from vosk import Model, KaldiRecognizer, SetLogLevel


class VoiceRecognition(sr.Recognizer):
    def __init__(self):
        super().__init__()

        self.online_recognition = False

        self.last_failed_recognition = None
        self.number_of_last_failed_recognition = 0

        model = Model(full_path_to_vosk_model)
        self.rec = KaldiRecognizer(model, 16000)

        self.dynamic_energy_threshold = False

        self.logger = logging.getLogger("VoiceRecognition")

        self.logger.info("VoiceRecognition initialized")

    def voice_recognition_loop(self):

        m = sr.Microphone()

        with m as source:
            self.adjust_for_ambient_noise(source)

        self.listen_in_background(m, self.callback)
        while True:
            time.sleep(0.1)

    def callback(self, recognizer, audio):
        try:
            print("Recognizing...")

            text = self._recognize_vosk(audio, self.rec)

            jarvis_words = ["jarvis", "judges",
                            "jonas", "jaromir", "chatter", "jarrod", "jeremy", "jerry", "cherries", "jefferson", "jennifer", "baroness", "jervis"]

            if text:
                text = text.removeprefix("the").strip()
                if any(text.lower().startswith(word) for word in jarvis_words):
                    text = self._recognize_google(audio)
                    voice_recognition_model.create(text=text)
                    self.logger.info(f"Розпізнано, текст: {text}")
                    self.analyze_text(text)

            print("Listening...")
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            self.logger.info(
                "Гугл не слухає( {0}".format(
                    e
                )
            )

    def _recognize_vosk(self, audio, rec):
        if audio is not None:
            buffer = audio.get_raw_data(convert_rate=16000, convert_width=2)
            rec.AcceptWaveform(buffer)

            result = json.loads(rec.FinalResult())
            return result["text"] if result["text"] else None

    def _recognize_google(self, audio):
        try:
            text = self.recognize_google(audio, language="uk-UA")
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            self.logger.info(
                "Гугл не слухає( {0}".format(
                    e
                )
            )
            return None

    def analyze_text(self, text):
        text = text.lower().strip()

        for module in modules:
            threading.Thread(target=module.analyze_text, args=(text,)).start()

    def start(self):
        threading.Thread(target=self.voice_recognition_loop).start()
