import tkinter as tk
from tkinter import messagebox
import random
from flashcards import flashcard_list, load_flashcards

stats = {"correct": 0, "total": 0}

def create_quiz_frame(container, show_frame):
    load_flashcards()
    frame = tk.Frame(container)
    question_label = tk.Label(frame, text="", font=("Helvetica", 14), wraplength=400)
    question_label.pack(pady=20)
    buttons = []
    def load_question():
        for b in buttons:
            b.destroy()
        buttons.clear()
        if len(flashcard_list) <= 4:
            question_label.config(text="Add at least 4 flashcards to play the quiz.")
            return

        correct = random.choice(flashcard_list)
        choices = random.sample(flashcard_list, 4)
        if correct not in choices:
            choices.pop()
            choices.append(correct)
        random.shuffle(choices)
        question_label.config(text=f"What is the Spanish word for: {correct[0]}?")
        for word in choices:
            b = tk.Button(
                frame, 
                text=word[1], 
                command=lambda w=word[1], c=correct[1]: check_answer(w, c)
                )
            b.pack(pady=2)
            buttons.append(b)
        


    def check_answer(selected, correct):
        stats["total"] += 1
        if selected == correct:
            messagebox.showinfo("Correct!", "Nice job!")
        else:
            messagebox.showinfo("Wrong!", f"The correct answer was: {correct}")
        load_question()

    tk.Button(frame, text="Back to Menu", command=lambda: show_frame("Main")).pack(pady=10)

    load_question()
    
    return frame