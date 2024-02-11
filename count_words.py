# Import the Tkinter module
from tkinter import *

# Function to handle the click event on the entry box
def on_entry_click(event):
    # Check if the current text is the default text
    if input_entry.get("1.0", "end-1c") == DEFAULT_TEXT:
        # If yes, delete the default text and change the background color
        input_entry.delete("1.0", "end-1c")
        input_entry.configure(bg="lightblue")

# Function to handle the hover event on the "Count" button
def on_count_hover(event):
    # Check if there is input text and it's not the default text
    if input_entry.get("1.0", "end-1c") != DEFAULT_TEXT and input_entry.get("1.0", "end-1c"):
        # Change the button appearance on hover
        count_button.configure(bg="green", fg="white", relief=SUNKEN)

# Function to handle the leave event on the "Count" button
def on_count_leave(event):
    # Check if there is input text and it's not the default text
    if input_entry.get("1.0", "end-1c") != DEFAULT_TEXT and input_entry.get("1.0", "end-1c"):
        # Change the button appearance on leave
        count_button.configure(bg="orange", fg="black", relief=SUNKEN)

# Function to handle the hover event on the "Clear" button
def on_clear_hover(event):
    # Check if there is input text and it's not the default text
    if input_entry.get("1.0", "end-1c") != DEFAULT_TEXT and input_entry.get("1.0", "end-1c"):
        # Change the button appearance on hover
        clear_button.configure(bg="green", relief=SUNKEN)

# Function to handle the leave event on the "Clear" button
def on_clear_leave(event):
    # Check if there is input text and it's not the default text
    if input_entry.get("1.0", "end-1c") != DEFAULT_TEXT and input_entry.get("1.0", "end-1c"):
        # Change the button appearance on leave
        clear_button.configure(bg="red", relief=SUNKEN)

# Function to handle the click event on the "Count" button
def on_click():
    # Check if there is input text and it's not the default text
    if input_entry.get("1.0", "end-1c") != DEFAULT_TEXT and input_entry.get("1.0", "end-1c"):
        # Count the number of words and display the result in the output label
        output_label.config(text="No. of words = " + str(len((input_entry.get("1.0", "end-1c")).split())), fg="green")
    else:
        # If no input, display an error message in the output label
        output_label.config(text="Enter input", fg="red")

# Function to handle the click event on the "Clear" button
def on_clear():
    # Check if there is input text and it's not the default text
    if input_entry.get("1.0", "end-1c") != DEFAULT_TEXT:
        # Clear the input text, reset background color, and focus on the window
        input_entry.delete("1.0", "end-1c")
        input_entry.insert("1.0", DEFAULT_TEXT)
        input_entry.configure(bg="white")
        window.focus_force()
    # Change the "Clear" button background color
    clear_button.configure(bg="red")
    # Clear the output label
    output_label.config(text="")

# Default text for the entry box
DEFAULT_TEXT = "Enter a sentence or paragraph to count no. of words    "

# Create the main Tkinter window
window = Tk()
# Set window size limits
window.geometry("350x350")
window.minsize(350, 350)
window.maxsize(350, 350)
# Set window title and icon
window.title("COUNT_WORDS")
window.wm_iconbitmap("count_words_favicon.ico")

# Set text box dimensions and font style
text_width = 30
text_height = 8
fontstyle = "Arial 12 bold"

# Create a Text widget for input
input_entry = Text(window, width=text_width, height=text_height, wrap="word", font=fontstyle)
input_entry.insert("1.0", DEFAULT_TEXT)
# Bind the entry click event to the function
input_entry.bind("<Button-1>", on_entry_click)
# Place the entry box in the window
input_entry.place(x=50, y=50)

# Create the "Count" button
count_button = Button(window, text="Count No. of Words", font=fontstyle, bg="orange", fg="black", command=on_click)
# Place the "Count" button in the window
count_button.place(x=60, y=230)
# Bind hover and leave events to the corresponding functions
count_button.bind("<Enter>", on_count_hover)
count_button.bind("<Leave>", on_count_leave)

# Create the "Clear" button
clear_button = Button(window, text="Clear", font=fontstyle, bg="red", fg="white", command=on_clear)
# Place the "Clear" button in the window
clear_button.place(x=250, y=230)
# Bind hover and leave events to the corresponding functions
clear_button.bind("<Enter>", on_clear_hover)
clear_button.bind("<Leave>", on_clear_leave)

# Create the output label
output_label = Label(window, text="", font="Arial 17 bold")
# Place the output label in the window
output_label.place(x=120, y=290)

# Start the Tkinter event loop
window.mainloop()
