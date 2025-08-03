# main.py - LangFlash Main Controller 

import os
import tkinter as tk
from PIL import Image, ImageTk
import editor 
import practice
import quiz
from flashcards import flashcards
#Import visual style from theme.py
from theme import *


# -------------------------------
#Create root window
root = tk.Tk()
root.title("LangFlash")
root.geometry("600x700")
root.config(bg=BG_COLOR)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


# -------------------------------
#Ensure data from flashcards is saved on exit (defined right after root exists)
def on_closing():
    flashcards.save()
    print("App is closing, saving flashcards...")
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# -------------------------------
#Create a container frame inside root to hold all app screens
container = tk.Frame(root, bg=BG_COLOR)
container.grid(row=0, column=0, sticky="nsew")

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)


#Dictionary to hold references to different screen frames
frames = {}


# -------------------------------
#Function to bring the requested frame to the front (visible)
def show_frame(name):
    frames[name].tkraise()


# -------------------------------
#Create the different frames

#Editor screen - create flashcards
frames["Editor"] = editor.create_editor_frame(container, show_frame)
frames["Editor"].grid(row=0, column=0, sticky="nsew")

#Practice screen - review flashcards
frames["Practice"] = practice.create_practice_frame(container, show_frame)
frames["Practice"].grid(row=0, column=0, sticky="nsew")

#Quiz screen - test knowledge
frames["Quiz"] = quiz.create_quiz_frame(container, show_frame)
frames["Quiz"].grid(row=0, column=0, sticky="nsew")


# -------------------------------
#Main Menu Frame
main_frame = tk.Frame(container, bg=BG_COLOR)
frames["Main"] = main_frame
main_frame.grid(row=0, column=0, sticky="nsew")

#Configure grid rows and columns to position content
main_frame.grid_rowconfigure(0, weight=0)
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_rowconfigure(2, weight=3)
main_frame.grid_columnconfigure(0, weight=1)


#Spacer frame at top
spacer_top = tk.Frame(main_frame, bg=BG_COLOR)
spacer_top.grid(row=0, column=0, sticky="nsew")

#Menu content frame at row 1
menu_content = tk.Frame(main_frame, bg=BG_COLOR)
menu_content.grid(row=1, column=0)

#Spacer frame at bottom
spacer_bottom = tk.Frame(main_frame, bg=BG_COLOR)
spacer_bottom.grid(row=2, column=0, sticky="nsew")


# -------------------------------
#Load and resize images
def load_image(filename, size):
    path = os.path.join("assets", filename)
    img = Image.open(path)
    img = img.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(img)

#Images
logo_img = load_image("icon_main_language.png", (140, 140))
flashcard_img = load_image("icon_editor_flashcard.png", (40, 40))
practice_img = load_image("icon_practice_work.png", (40, 40))
quiz_img = load_image("icon_quiz_question.png", (40, 40))
exit_img = load_image("exit.png", (20, 20))

#Prevent garbage collection
image_refs = [logo_img, flashcard_img, practice_img, quiz_img, exit_img]
# -------------------------------
#Add widgets inside menu_content frame

#Title label
tk.Label(menu_content, bg=BG_COLOR).pack(padx=10)
tk.Label(menu_content, text="LangFlash - English-Spanish Trainer", font=TITLE_FONT, fg=TITLE_COLOR, bg=BG_COLOR).pack(pady=15)
logo_label = tk.Label(menu_content, image=logo_img, bg=BG_COLOR)
logo_label.image = logo_img
logo_label.pack(pady=(10, 20))

# Helper to create styled button with hover
def create_hover_button(parent, text, command=None, image = None, compound = None, style=button_style_main):
    btn = tk.Button(parent, text=text, command=command, image = image, compound = compound, **style)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    btn.pack(pady=5)
    return btn

# Helper to create styled button with hover for exit button
def create_hover_button2(parent, text, command= None, image=None, compound = None, style2=button_style_main2):
    btn = tk.Button(parent, text=text, command=command, image = image, compound = compound, **style2)
    btn.bind("<Enter>", on_enter2)
    btn.bind("<Leave>", on_leave2)
    btn.pack(pady=55)
    return btn


#Button to switch to Editor screen (flashcard creation)
create_hover_button(menu_content, text="Create Flashcards", image=flashcard_img, compound= "left", command=lambda: show_frame("Editor"))


#Button to switch to Practice screen (review mode)
create_hover_button(menu_content, text="Practice Mode", image=practice_img, compound= "left", command=lambda: show_frame("Practice"))


#Button to switch to Quiz screen (quiz mode)
create_hover_button(menu_content, text="Quiz Mode", image=quiz_img, compound= "left", command=lambda: show_frame("Quiz"))


#Button to close the application
create_hover_button2(menu_content, text="Exit", image=exit_img, compound= "left", command=on_closing)


# -------------------------------
#Show the main menu frame when app starts
show_frame("Main")


# -------------------------------
#Start tkinter 
root.mainloop()