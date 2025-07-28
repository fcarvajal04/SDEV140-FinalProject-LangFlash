import tkinter as tk
from flashcards import flashcards
#Import visual style from theme.py
from theme import *


index = 0
flipped = False

def create_practice_frame(container, show_frame):
    flashcards.load()
    
    frame = tk.Frame(container, bg = BG_COLOR)
    index = 0
    flipped = False

    label = tk.Label(frame, text="", font=HEADER_FONT, bg=BG_COLOR, fg=FONT_COLOR)
    label.pack(pady=30)

    def show_card():
        global index, flipped
        if not flashcards.flashcard_list:
            label.config(text="No flashcards available.")
            return
        flipped = False
        label.config(text=flashcards.flashcard_list[index][0])

    def flip():
        global flipped
        if not flashcards.flashcard_list:
            return
        flipped = not flipped
        if flipped:
            label.config(text=flashcards.flashcard_list[index][1])
        else:
            label.config(text=flashcards.flashcard_list[index][0])

    def next_card():
        global index, flipped
        if not flashcards.flashcard_list:
            return
        index = (index + 1) % len(flashcards.flashcard_list)
        flipped = False
        label.config(text=flashcards.flashcard_list[index][0])

    def make_btn(text, command):
        btn = tk.Button(frame, text=text, command=command, **button_style)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.pack(pady=5)
        return btn
    
    def make_btn2(text, command):
        btn = tk.Button(frame, text=text, command=command, **button_style2)
        btn.bind("<Enter>", on_enter2)
        btn.bind("<Leave>", on_leave2)
        btn.pack(pady=10)
        return btn

    make_btn("Flip", command = flip)
    make_btn("Next", command = next_card)
    make_btn2("Back to Menu", lambda: show_frame("Main"))
    
    show_card()
    return frame
