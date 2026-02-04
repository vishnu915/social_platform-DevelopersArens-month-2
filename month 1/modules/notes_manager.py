import json
import os
from datetime import datetime


class NotesManager:
    FILE = "data/notes.json"

    def __init__(self):
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists(self.FILE):
            with open(self.FILE, "r") as f:
                self.notes = json.load(f)
        else:
            self.notes = []

    def save_notes(self):
        with open(self.FILE, "w") as f:
            json.dump(self.notes, f, indent=2)

    def add_note(self):
        title = input("Title: ")
        content = input("Content: ")

        note = {
            "id": len(self.notes) + 1,
            "title": title,
            "content": content,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.notes.append(note)
        self.save_notes()
        print("✅ Note added")

    def view_notes(self):
        if not self.notes:
            print("No notes found")
            return
        for n in self.notes:
            print(f"\n[{n['id']}] {n['title']}")
            print(n["content"])

    def run(self):
        while True:
            print("\n--- Notes Manager ---")
            print("1. View Notes")
            print("2. Add Note")
            print("3. Back")

            choice = input("Choice: ")

            if choice == "1":
                self.view_notes()
            elif choice == "2":
                self.add_note()
            elif choice == "3":
                break
            else:
                print("Invalid choice")
