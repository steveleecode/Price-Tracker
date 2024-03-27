import tkinter as tk
import tkinter.font as font
from tkinter import *

# Create the main application window
root = tk.Tk()
root.title("Amazon Price Tracker")  # Set the title of the window
root.size()
root.geometry("600x400")
root.resizable(False, False)

title = font.Font(size=25)
body = font.Font(size=12)

# Create a label widget
label = tk.Label(root, text="Amazon Price Tracker", font=title)
label.pack(anchor='center')  # Use pack() method to add the label to the window

label = tk.Label(root, text = "Input URL to an Amazon Product", font=body)
label.place(x=183, y=70)

url = Entry(root, width = 90)
url.place(x=27, y=100)

# Create a function to handle button click event
def button_click():
    priceTrack()

# Create a button widget
button = tk.Button(root, text="Click Me", command=button_click)
button.place(x=100, y=300)  # Add the button to the window

# Run the Tkinter event loop
root.mainloop()