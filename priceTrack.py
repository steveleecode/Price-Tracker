# importing necessary packages
from bs4 import BeautifulSoup
import requests
import keyboard
import time
import sys
from datetime import datetime

def ping_website(url):
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


def priceTrack():
    url = input("Input a URL to Price Track: ")
    if not ping_website(url):
        priceTrack()
    
    previousPrice = None
    iterations = 0
    while(not keyboard.is_pressed('p')):
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

    print("Exiting Program")
    #closing the driver
    sys.exit(1)

if __name__ == "__main__":
    priceTrack()