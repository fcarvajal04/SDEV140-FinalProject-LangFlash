# quiz.py - Screen for knowledge testing using multiple choice quiz format

import tkinter as tk
from tkinter import messagebox
import random
from flashcards import flashcards
#Import visual style from theme.py
from theme import *


#Variable to track correct answers
stats = {"correct": 0, "total": 0}

#Variable to track direction (English to Spanish or Spanish to English)
direction = "ENG_TO_SPAN"

#Function to create and start quiz
def create_quiz_frame(container, show_frame):
    flashcards.load()
    frame = tk.Frame(container, bg = BG_COLOR)
    
    #Variable to track correct answers
    stats = {"correct": 0, "total": 0}
    #Variable to track direction (English to Spanish or Spanish to English)
    direction = "ENG_TO_SPAN"

    # Widgets that start hidden:
    score_label = tk.Label(frame, text="Score 0 / 0", font=BUTTON_FONT, bg=BG_COLOR, fg=TITLE_COLOR)
    question_label = tk.Label(frame, text="", font=HEADER_FONT, wraplength=400, bg=BG_COLOR, fg=FONT_COLOR)
    buttons = []

    # Toggle direction button (starts hidden)
    toggle_button = tk.Button(frame, text="Switch to Spanish → English", **button_style)
    direction_label = tk.Label(frame, text="Quiz Mode: English → Spanish")

    # Start Quiz button (visible initially)
    start_button = tk.Button(frame, text="Start Quiz", **button_style)
    start_button.pack(pady=10)

    # Back to Menu button (always visible)
    back_button = tk.Button(frame, text="Back to Menu", command=lambda: show_frame("Main"), **button_style2)
    back_button.pack(pady=10)


    def toggle_direction():
        nonlocal direction
        if direction == "ENG_TO_SPAN":
            direction = "SPAN_TO_ENG"
            toggle_button.config(text = "Switch to English → Spanish")
            direction_label.config(text = "Quiz Mode: Spanish → English")
        else:
            direction = "ENG_TO_SPAN"
            toggle_button.config(text = "Switch to Spanish → English")
            direction_label.config(text = "Quiz Mode: English → Spanish")
        stats["correct"] = 0
        stats["total"] = 0
        score_label.config(text="Score: 0 / 0")

        load_question()

    toggle_button.config(command=toggle_direction)
    toggle_button.bind("<Enter>", on_enter)
    toggle_button.bind("<Leave>", on_leave)
    
    def load_question():
        for b in buttons:
            b.destroy()
        buttons.clear()

        if len(flashcards.flashcard_list) <= 4:
            question_label.config(text="Add at least 4 flashcards to play the quiz.")
            return

        correct = random.choice(flashcards.flashcard_list)
        choices = random.sample(flashcards.flashcard_list, 4)
        if correct not in choices:
            choices.pop()
            choices.append(correct)
        random.shuffle(choices)

        if direction == "ENG_TO_SPAN":
            question_label.config(text=f"What is the Spanish word for: {correct[0]}?")
            correct_answer = correct[1]
            answer_choices = [word[1] for word in choices]
        else:
            question_label.config(text=f"What is the English word for: {correct[1]}?")
            correct_answer = correct[0]
            answer_choices = [word[0] for word in choices]

        for word in answer_choices:
            b = tk.Button(
                frame, 
                text=word, **button_style, 
                command=lambda w=word, c=correct_answer: check_answer(w, c))
            b.bind("<Enter>", on_enter)
            b.bind("<Leave>", on_leave)
            b.pack(pady=2)
            buttons.append(b)

        score_label.config(text=f"Score: {stats['correct']} / {stats['total']}")
    
    def check_answer(selected, correct):
        stats["total"] += 1
        if selected == correct:
            stats["correct"] += 1
            messagebox.showinfo("Correct!", "Nice job!")
        else:
            messagebox.showinfo("Wrong!", f"The correct answer was: {correct}")
        load_question()
    
    def start_quiz():
        # Hide start button
        start_button.pack_forget()

        # Show quiz widgets
        direction_label.pack()
        toggle_button.pack(pady=10)
        score_label.pack(pady=5)
        question_label.pack(pady=20)

        # Load first question
        load_question()

    start_button.config(command=start_quiz)
    
    return frame