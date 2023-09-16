import datetime
import json


class NoteEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Note):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)


class Note:
    def __init__(self, number: int, name: str, body: str):
        self.__note = {
            'id': str(number),
            'name': name,
            'body': body,
            'lastdate': str(datetime.datetime.now(tz=None)).partition(".")[0]
        }

    def get_note(self):
        return self.__note

    def get_id(self):
        return self.__note.get('id')
