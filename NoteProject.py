from Notebook import *
from Note import *


notebook = Notebook()
while True:
    print("Choose the operation(press a number):\n"
          "1. Print the notebook\n"
          "2. Sort the notebook\n"
          "3. Add new note\n"
          "4. Change some note\n"
          "5. Delete some note\n"
          "6. Save changes\n"
          "7. End the process")
    action = input()
    if action == "1":
        notebook.print()
    elif action == "2":
        notebook.sort()
        print("The notebook is sorted")
    elif action == "3":
        name = input("Enter name of the note:\n")
        body = input("Write content of the note:\n")
        num = int(input())
        note = Note(num, name, body)
        notebook.append(note)
    elif action == "4":
        num = input("What note you want to change?(enter the ID)\n")
        notebook.change(num)
    elif action == "5":
        num = input("Enter ID of note which you want to delete:\n")
        notebook.remove(num)
    elif action == "6":
        notebook.save()
    elif action == "7":
        break


