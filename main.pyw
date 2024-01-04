import logging
from speach_recognition import VoiceRecognition
from models import Logs

# make all loggers messages show up in the terminal
logging.basicConfig(level=logging.INFO)
# make all loggers messages log into the database
logging.getLogger().addHandler(Logs.handler())




VoiceRecognition().start()
