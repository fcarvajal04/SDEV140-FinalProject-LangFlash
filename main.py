# main.py - LangFlash Main Controller 

import tkinter as tk
import editor 
import practice
import quiz 


# -------------------------------
#Style Settings - Constants for colors and fonts
#COLORS
BG_COLOR = "#fefefe"
BTN_COLOR = "#85A8D0"
BTN_HOVER = "#C4D9F0"
TITLE_COLOR = "#4B6C9C"
FONT_COLOR = "#2E3D59" 
WARNING_COLOR = "#FF6B6B"
FONT_MAIN = ("Helvetica", 16)
FONT_TITLE = ("Helvetica", 24, "bold")

#FONTS
TITLE_FONT = ("Georgia", 28, "bold italic")
HEADER_FONT = ("Segoe UI", 16, "bold")
BODY_FONT = ("Calibri", 12)
BUTTON_FONT = ("Calibri", 12)


# -------------------------------
#Create root window
root = tk.Tk()
root.title("LangFlash")
root.geometry("600x500")
root.config(bg=BG_COLOR)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


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
#Add widgets inside menu_content frame

#Title label
tk.Label(menu_content, text="LangFlash - English-Spanish Trainer", font=TITLE_FONT, fg=TITLE_COLOR, bg=BG_COLOR).pack(pady=20)


#Styled button dictionaries
button_style = {
    "font": BUTTON_FONT,
    "bg": "#85A8D0",
    "fg": "black",
    "width": 20,
    "padx": 10,
    "pady": 5
}

button_style2 = {
    "font": BUTTON_FONT,
    "bg": "#85A8D0",
    "fg": WARNING_COLOR,
    "width": 10,
    "padx": 5,
    "pady": 2
}
#Button to switch to Editor screen (flashcard creation)
tk.Button(menu_content, text="Create Flashcards", command=lambda: show_frame("Editor"), **button_style).pack(pady=5)


#Button to switch to Practice screen (review mode)
tk.Button(menu_content, text="Practice Mode", command=lambda: show_frame("Practice"), **button_style).pack(pady=5)


#Button to switch to Quiz screen (quiz mode)
tk.Button(menu_content, text="Quiz Mode", command=lambda: show_frame("Quiz"), **button_style).pack(pady=5)


#Button to close the application
tk.Button(menu_content, text="Exit", command=root.destroy, **button_style2).pack(pady=110)


# -------------------------------
#Show the main menu frame when app starts
show_frame("Main")


# -------------------------------
#Start tkinter 
root.mainloop()