# editor.py - Screen for adding new flashcards

import tkinter as tk
from tkinter import messagebox
from flashcards import flashcard_list, save_flashcards, load_flashcards, delete_all_flashcards


#Style Settings - Constants for colors and fonts
BG_COLOR = "#fdf6e3"
BTN_COLOR = "#eded12"
FONT_COLOR = "#333333"
FONT_MAIN = ("Helvetica", 12)
FONT_TITLE = ("Helvetica", 20, "bold")


#Create editor screen
def create_editor_frame(container, show_frame):
    frame = tk.Frame(container, bg=BG_COLOR)

    #Title
    tk.Label(frame, text="Create Flashcards", font=FONT_TITLE).pack(pady=10)

    #Entry for English word
    tk.Label(frame, text = "English word: ", font=FONT_MAIN).pack()
    entry_eng = tk.Entry(frame)
    entry_eng.pack()

    #Entry for Spanish word
    tk.Label(frame, text = "Spanish word: ", font=FONT_MAIN).pack()
    entry_span = tk.Entry(frame)
    entry_span.pack()
    

    #Function to add a new card
    def add_card():
        eng = entry_eng.get().strip()
        span = entry_span.get().strip()
        if not eng or not span:
            messagebox.showwarning("Invalid Input", "Both fields must be filled!")
            return
        flashcard_list.append((eng, span))
        save_flashcards()
        messagebox.showinfo("Saved", f"Added: {eng} → {span}")
        
        #Clear inputs
        entry_eng.delete(0, tk.END)
        entry_span.delete(0, tk.END)
    

    #Function to delete all flashcards
    def confirm_delete():
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete ALL flashcards?")
        if confirm:
            delete_all_flashcards()
            messagebox.showinfo("Deleted", "All flashcards have been deleted successfully.")


    #Function to open a new window and display saved flashcards
    def open_flashcard_viewer():
        viewer = tk.Toplevel()
        viewer.title("Saved Flashcards")
        viewer.geometry("350x450")
        viewer.configure(bg="#fdf6e3")

        tk.Label(viewer, text="All Flashcards", font=FONT_MAIN, bg=BG_COLOR).pack(pady=10)

        list_frame = tk.Frame(viewer, bg="#fdf6e3")
        list_frame.pack(pady=5)

        load_flashcards()

        if not flashcard_list:
            tk.Label(list_frame, text="No flashcards found.", bg="#fdf6e3").pack()
        else:
            for i, (eng, span) in enumerate(flashcard_list):
                # Show both English and Spanish
                text = f"{i+1}. {eng} → {span}"
                tk.Label(list_frame, text=text, font=("Helvetica", 12), anchor="w", bg="#fdf6e3").pack(fill="x", padx=10, pady=2)


    #Add buttons
    tk.Button(frame, text="Add Flashcard", command=add_card).pack(pady=5)
    tk.Button(frame, text="View All Flashcards", command=open_flashcard_viewer).pack(pady=5)
    tk.Button(frame, text="Delete All Flashcards", command=confirm_delete, fg="red", bg="#FF6B6B").pack(pady=5)
    tk.Button(frame, text="Back to Menu", command=lambda: show_frame("Main")).pack(pady=5)


    return frame
