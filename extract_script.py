#import Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 

from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

import time 

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

#let's go to a website where we can extract something 
driver.get("https://quotes.toscrape.com/")

f = open("store.txt", "w")

#set flag
flag = 0

while flag == 0:

    #first find the class that contains all the quotes
    quotes = driver.find_elements(By.CLASS_NAME, "quote")   

    #next go through all the quotes and find the quote by the correct author
    for quote in quotes:
        author = quote.find_element(By.CLASS_NAME, "author").text

        #in this case, we're looking for albert einstein
        if author == "J.K. Rowling":
            quote_text = quote.find_element(By.CLASS_NAME, "text").text
            #print it to the console for us to see
            f.write(quote_text + "Is said by: " + author + "\n")
            
    
    # After processing all quotes on the current page, check if there's a next page
    try:
        next_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Next")
        next_button.click()  # Click the "Next" button to go to the next page
        time.sleep(5)  # Wait for the next page to load
        
    except:
        # If there's no "Next" button, we've reached the last page
        print("Reached the end of pages, quote not found.")
        flag = 1

time.sleep(5)
f.close() 
driver.quit()

#So this code effectively goes into a website that has quotes by a specific author and prints to a store.txt file


