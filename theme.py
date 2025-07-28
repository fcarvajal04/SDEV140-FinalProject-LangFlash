# theme.py – Style constants for LangFlash

#Colors
BG_COLOR = "#fefefe"
BTN_COLOR = "#85A8D0"
BTN_HOVER = "#C4D9F0"
TITLE_COLOR = "#4B6C9C"
FONT_COLOR = "#2E3D59"
WARNING_COLOR = "#FF6B6B"
ENTER_WARNING = "#FF0202"

#Fonts
TITLE_FONT = ("Georgia", 28, "bold italic")
HEADER_FONT = ("Segoe UI", 16, "bold")
BODY_FONT = ("Calibri", 12)
BUTTON_FONT = ("Calibri", 12)

#Shared button hover functions
def on_enter(event):
    event.widget['background'] = BTN_HOVER
    event.widget['fg'] = TITLE_COLOR  # Change text color on hover
    event.widget['relief'] = "groove"  # Add subtle border effect

def on_leave(event):
    event.widget['background'] = BTN_COLOR
    event.widget['fg'] = FONT_COLOR
    event.widget['relief'] = "raised"

def on_enter2(event): #For buttons with red text
    event.widget['background'] = BTN_HOVER
    event.widget['fg'] = ENTER_WARNING 
    event.widget['relief'] = "groove"  

def on_leave2(event): #For buttons with red text
    event.widget['background'] = BTN_COLOR
    event.widget['fg'] =  WARNING_COLOR
    event.widget['relief'] = "raised"

#Styled button dictionaries
button_style = {
    "font": BUTTON_FONT,
    "bg": BTN_COLOR,
    "fg": "black",
    "activebackground": BTN_HOVER,
    "width": 20,
    "padx": 10,
    "pady": 5,
    "relief" : "raised",
    "bd": 2
}

button_style2 = {
    "font": BUTTON_FONT,
    "bg": BTN_COLOR,
    "fg": WARNING_COLOR,
    "activebackground": BTN_HOVER,
    "width": 15,
    "padx": 5,
    "pady": 5,
    "relief": "raised",
    "bd": 2
}
