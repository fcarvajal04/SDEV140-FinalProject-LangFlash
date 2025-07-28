# editor.py - Screen for adding new flashcards

import tkinter as tk
from tkinter import messagebox
from flashcards import flashcards
#Import visual style from theme.py
from theme import *

#Create editor screen
def create_editor_frame(container, show_frame):
    frame = tk.Frame(container, bg=BG_COLOR)

    #Title
    tk.Label(frame, text="Create Flashcards", font=HEADER_FONT, fg=TITLE_COLOR, bg=BG_COLOR).pack(pady=10)

    #Entry for English word
    tk.Label(frame, text = "English word: ", font=BODY_FONT, fg=FONT_COLOR, width = 10).pack()
    entry_eng = tk.Entry(frame)
    entry_eng.pack()

    #Entry for Spanish word
    tk.Label(frame, text = "Spanish word: ", font=BODY_FONT, fg=FONT_COLOR, width = 10).pack()
    entry_span = tk.Entry(frame)
    entry_span.pack()
    

    #Function to add a new card
    def add_card():
        eng = entry_eng.get().strip()
        span = entry_span.get().strip()
        if not eng or not span:
            messagebox.showwarning("Invalid Input", "Both fields must be filled!")
            return
        
        flashcards.add(eng, span)
        flashcards.save()
        messagebox.showinfo("Saved", f"Added: {eng} → {span}")
        
        #Clear inputs
        entry_eng.delete(0, tk.END)
        entry_span.delete(0, tk.END)
    

    #Function to delete all flashcards
    def confirm_delete():
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete ALL flashcards?")
        if confirm:
            flashcards.delete_all()
            flashcards.save()
            messagebox.showinfo("Deleted", "All flashcards have been deleted successfully.")


    #Function to open a new window and display saved flashcards
    def open_flashcard_viewer():
        viewer = tk.Toplevel()
        viewer.title("Saved Flashcards")
        viewer.geometry("350x450")
        viewer.configure(bg=BG_COLOR)

        tk.Label(viewer, text="All Flashcards", font=HEADER_FONT, fg=TITLE_COLOR, bg=BG_COLOR).pack(pady=10)

        list_frame = tk.Frame(viewer, bg=BG_COLOR)
        list_frame.pack(pady=5)

        flashcards.load()

        if not flashcards.flashcard_list:
            tk.Label(list_frame, text="No flashcards found.", bg=BG_COLOR).pack()
        else:
            for i, (eng, span) in enumerate(flashcards.flashcard_list):
                # Show both English and Spanish
                text = f"{i+1}. {eng} → {span}"
                tk.Label(list_frame, text=text, font=(BODY_FONT), anchor="w", bg=BG_COLOR).pack(fill="x", padx=10, pady=2)

    # Styled buttons
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
    
    #Add buttons
    make_btn(text="Add Flashcard", command=add_card)
    make_btn(text="View All Flashcards", command=open_flashcard_viewer)
    make_btn2(text="Delete All Flashcards", command=confirm_delete)
    make_btn(text="Back to Menu", command=lambda: show_frame("Main"))


    return frame
