from peewee import SqliteDatabase, Model, TextField, IntegerField, BooleanField, ForeignKeyField, DateTimeField
from settings import database_file
import datetime
import logging

db = SqliteDatabase(database_file)

class BaseModel(Model):
    class Meta:
        database = db

class voice_recognition_model(BaseModel):
    text = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

class Logs(BaseModel):
    text = TextField()
    module = TextField(default="NoModule")
    created_at = DateTimeField(default=datetime.datetime.now)

    class handler(logging.Handler):
        def emit(self, record):
            Logs.create(text=record.msg, module=record.name)

db.create_tables([voice_recognition_model, Logs])