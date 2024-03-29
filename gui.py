import tkinter as tk
import tkinter.font as font
from tkinter import *
from bs4 import BeautifulSoup
import requests
import keyboard
import time
import sys
from datetime import datetime

def pingWebsite(url):
    try:
        response = requests.get(url)
        session = requests.Session()
        session.verify = False

        if response.status_code == 200:
            item = BeautifulSoup(response.content, "html.parser").find(id="productTitle")
            print(f"Found Product: {item.getText().lstrip()}")
            return True
        else:
            print(f"Website is unreachable (Status code: {response.status_code}).")
            return False
    except (requests.ConnectionError, requests.exceptions.MissingSchema):
        print(f"Website is unreachable.")
        return False

def flash_label(label):
    if label.cget("foreground") == "red":
        label.config(foreground="black")
    else:
        label.config(foreground="red")
    label.after(500, flash_label, label)

def main_gui():
    # Create the main application window
    root = tk.Tk()
    root.title("Amazon Price Tracker")  # Set the title of the window
    root.size()
    root.geometry("600x400")
    root.resizable(False, False)

    title = font.Font(size=25)
    body = font.Font(size=12)
    trackFont = font.Font(size=9)
    errorFont = font.Font(size=9, weight='bold')

    # Create a label widget
    label = tk.Label(root, text="Amazon Price Tracker", font=title)
    label.pack(anchor='center')  # Use pack() method to add the label to the window

    label = tk.Label(root, text = "Input URL to an Amazon Product", font=body)
    label.place(relx=0.5, rely=0.18, anchor=CENTER)

    error = tk.Label(root, font=errorFont, fg="red")
    error.place(relx=0.5, rely=0.125, anchor=CENTER)

    url = Entry(root, width = 90)
    url.place(relx=0.5, rely=0.25, anchor=CENTER)

    labelframe = LabelFrame(root, text="Price Tracker")

    timeLabel = Label(root)
    timeLabel.place(relx=0.5, rely = 0.975, anchor=CENTER)

    def clock():
        t = datetime.now().strftime("Current Time: %H:%M:%S")
        timeLabel['text'] = t
        root.after(1000, clock) # run itself again after 1000 ms
    clock()

    # Create a function to handle button click event
    def button_click():
        if not pingWebsite(url.get()):
            error['text'] = "Website is Unreachable. Try again."
            flash_label(error)
            return

        labelframe.pack(fill="both", expand="yes", padx=100, pady=(125, 50))
        leftAlignTrack = 0.025

        productTitle = tk.Label(labelframe, text = "Product Name: ", font=trackFont)
        productTitle.place(relx=leftAlignTrack, rely=0.05)
        productPrice = tk.Label(labelframe, text = "Current Price: ", font=trackFont)
        productPrice.place(relx=leftAlignTrack, rely=0.2)

        titleBox = tk.Label(labelframe, font=trackFont)
        titleBox.place(relx=leftAlignTrack + 0.3, rely=0.05)
        priceBox = tk.Label(labelframe, font=trackFont)
        priceBox.place(relx=leftAlignTrack + 0.3, rely=0.05)




        #PRICETRACKER
        if not pingWebsite(url.get()):
            return False
        while(True):
            #Special Config for Amazon
            HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})
            response = requests.get(url.get(), headers=HEADERS)
            soup = BeautifulSoup(response.content, "html.parser")
            
            prices = soup.find_all("span", attrs={"class":'aok-offscreen'})
            name = soup.find(id="productTitle")
            titleBox['text'] = name
            realPrice = ""
            
            for price in prices:
                priceText = price.getText().lstrip().rstrip()
                if len(priceText) < 8:
                    realPrice = priceText
                    break
            
            priceBox['text'] = realPrice
            time.sleep(5)

    # Create a button widget
    button = tk.Button(root, text="Begin Tracking", command=button_click)
    button.place(relx = 0.5, rely = 0.35, anchor=CENTER)  # Add the button to the window


    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main_gui()