# importing necessary packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import ping, socket
import keyboard
import time


def main():
    url = input("Input a URL to Price Track")
    try:
        ping.verbose_ping(url, count=3)
    except socket.error:
        print("Invalid Input")
        main()
    
    while(not keyboard.is_pressed('p')):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)
        price = driver.find_elements(By.CLASS_NAME, "aok-offscreen")
        item = driver.find_elements(By.CLASS_NAME, "a-size-large product-title-word-break")
        print(f"Current price of {item} is {price}")
        time.sleep(5000)

    #closing the driver
    driver.close()

main()