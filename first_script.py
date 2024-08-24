#import selenium
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service\

#import time package so we can delay the stuff we do or work on
import time


#initialize your webdriver for chrome 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


#let's go to a website
driver.get("https://www.google.ca/")

#add delay to see what's going on
time.sleep(10)

driver.quit()