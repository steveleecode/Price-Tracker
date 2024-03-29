import tkinter as tk
import tkinter.font as font
from tkinter import *
from priceTrack import *
def pingWebsite(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            item = BeautifulSoup(response.content, "html.parser").find(id="productTitle")
            print(f"Found Product: {item.getText().lstrip()}")
            return True
        else:
            print(f"Website is unreachable (Status code: {response.status_code}).")
            return False
    except requests.ConnectionError:
        print(f"Website is unreachable.")
        return False

def main_gui():
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

    labelframe = LabelFrame(root, text="Price of your Item")

    tracker = priceTrack()
    # Create a function to handle button click event
    def button_click():
        labelframe.pack(fill="both", expand="yes", padx=100, pady=(125, 50))
        #PRICETRACKER
        if not pingWebsite(url):
            return False
        previousPrice = None
        iterations = 0
        while(True):
            #Special Config for Amazon
            HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})
            response = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(response.content, "html.parser")
            
            prices = soup.find_all("span", attrs={"class":'aok-offscreen'})
            name = soup.find(id="productTitle")
            realPrice = ""
            
            for price in prices:
                priceText = price.getText().lstrip().rstrip()
                if len(priceText) < 8:
                    realPrice = priceText
                    break
                
            current_time = datetime.now().strftime("%I:%M:%S %p")
            
            if iterations > 0 and not realPrice == previousPrice:
                print(f"Price Changed to {realPrice} at {current_time}")
            else:
                print(f"Current Price is {realPrice} at {current_time}")
            iterations += 1
            previousPrice = realPrice
            time.sleep(5)

    # Create a button widget
    button = tk.Button(root, text="Click Me", command=button_click)
    button.place(relx = 0.5, rely = 0.35, anchor=CENTER)  # Add the button to the window


    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main_gui()