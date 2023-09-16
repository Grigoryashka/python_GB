import Note
from Note import NoteEncoder
import json
import datetime


class Notebook:

    def __init__(self):
        with open("notebook.json", "r") as f:
            self.__notebook = json.load(f)
            print(self.__notebook)

    def append(self, note: Note):
        self.__notebook[note.get_id()] = note.get_note()

    def change(self, num):
        attribute = input("what do you want to change?\n"
                       "Name(n) or body(b)?\n")
        if attribute == "n":
            name = input("Enter new name:\n")
            self.__notebook[num]['name'] = name
            self.__notebook[num]['lastdate'] = str(datetime.datetime.now(tz=None)).partition(".")[0]
        elif attribute == "b":
            option = input("You want to rewrite(1) content or add something(2)?\n")
            body = self.__notebook[num]['body']
            if option == "1":
                body = input("Write new content:\n")
            elif option == "2":
                body = self.__notebook[num]['body'] + input("Write content to add:\n")
            self.__notebook[num]['body'] = body
            self.__notebook[num]['lastdate'] = str(datetime.datetime.now(tz=None)).partition(".")[0]

    def remove(self, num):
        self.__notebook.pop(num)

    def sort(self):
        self.__notebook = dict(reversed(sorted(self.__notebook.items(), key=lambda item: item[1].get('lastdate'))))

    def save(self):
        with open("notebook.json", "w") as f:
            json.dump(self.__notebook, f, cls=NoteEncoder)

    def print(self):
        for note in self.__notebook.values():
            print(note)
