# flashcards.py - Manage the flashcard list and file saving/loading

import json
import os


#File where flashcards will be saved
flashcard_file = "flashcards.json"
flashcard_list = []  # Format: [("dog", "perro"), ("cat", "gato")]


#Load flashcards from the JSON file
def load_flashcards():
    global flashcard_list
    if os.path.exists(flashcard_file):
        with open(flashcard_file, "r") as file:
            try:
                data = json.load(file)
                flashcard_list = [(item["english"], item["spanish"]) for item in data]
            except json.JSONDecodeError:
                flashcard_list = []
    else:
        flashcard_list = []


#Save current flashcards to JSON file
def save_flashcards():
    with open(flashcard_file, "w") as file:
        json.dump(
            [{"english": eng, "spanish": span} for eng, span in flashcard_list],
            file,
            indent=4
        )


#Load existing flashcards immediately when file is imported
load_flashcards()


#Feature to delete all flashcards
def delete_all_flashcards():
    global flashcard_list
    flashcard_list = []
    with open(flashcard_file, "w") as file:
        json.dump([], file)