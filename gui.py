import tkinter as tk
import tkinter.font as font

# Create the main application window
root = tk.Tk()
root.title("Amazon Price Tracker")  # Set the title of the window
root.size()
root.geometry("600x400")

f = font.Font(size=25)

# Create a label widget
label = tk.Label(root, text="Amazon Price Tracker", font=f)
label.pack()  # Use pack() method to add the label to the window

# Create a function to handle button click event
def button_click():
    label.config(text="Button clicked!")

# Create a button widget
button = tk.Button(root, text="Click Me", command=button_click)
button.pack()  # Add the button to the window

# Run the Tkinter event loop
root.mainloop()