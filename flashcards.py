# flashcards.py - Manage the flashcard list and file saving/loading

import json
import os

class FlashcardManager:
    def __init__(self):
        self.flashcard_file = "flashcards.json"
        self.flashcard_list = []
        self.load()

    def load(self):
        if os.path.exists(self.flashcard_file):
            with open(self.flashcard_file, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    self.flashcard_list = [(item["english"], item["spanish"]) for item in data]
                    print(f"Loaded {len(self.flashcard_list)} flashcards.")
                except json.JSONDecodeError:
                    print("JSON decode error — starting with empty list.")
                    self.flashcard_list = []
        else:
            self.flashcard_list = []

    def save(self):
        with open(self.flashcard_file, "w", encoding="utf-8") as file:
            json.dump(
                [{"english": eng, "spanish": span} for eng, span in self.flashcard_list],
                file,
                indent=4,
                ensure_ascii=False
            )
            print("Flashcards saved.")

    def add(self, english, spanish):
        if english and spanish:
            self.flashcard_list.append((english.strip(), spanish.strip()))
        print(f"Added: {english} → {spanish}")


    def delete_all(self):
        self.flashcard_list = []
        with open(self.flashcard_file, "w", encoding="utf-8") as file:
            json.dump([], file)
        print("All flashcards deleted.")

# Global instance
flashcards = FlashcardManager()
