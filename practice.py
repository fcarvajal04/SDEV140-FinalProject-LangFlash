import tkinter as tk
from flashcards import flashcard_list

index = 0
flipped = False

def create_practice_frame(container, show_frame):
    frame = tk.Frame(container)

    label = tk.Label(frame, text="", font=("Helvetica", 16))
    label.pack(pady=30)

    def show_card():
        global index, flipped
        if not flashcard_list:
            label.config(text="No flashcards available.")
            return
        flipped = False
        label.config(text=flashcard_list[index][0])

    def flip():
        global flipped
        if not flashcard_list:
            return
        flipped = not flipped
        if flipped:
            label.config(text=flashcard_list[index][1])
        else:
            label.config(text=flashcard_list[index][0])

    def next_card():
        global index, flipped
        if not flashcard_list:
            return
        index = (index + 1) % len(flashcard_list)
        flipped = False
        label.config(text=flashcard_list[index][0])

    tk.Button(frame, text="Flip", command=flip).pack()
    tk.Button(frame, text="Next", command=next_card).pack(pady=5)
    tk.Button(frame, text="Back to Menu", command=lambda: show_frame("Main")).pack(pady=10)

    show_card()
    return frame
