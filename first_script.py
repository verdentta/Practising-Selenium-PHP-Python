#import selenium
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service

#use this import to search stuff in the html
from selenium.webdriver.common.by import By 

#import in package that will help with typing, for example hitting the enter key 
from selenium.webdriver.common.keys import Keys 

#import for a package that helps to wait for UI to load in
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#import time package so we can delay the stuff we do or work on
import time


#initialize your webdriver for chrome 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


#let's go to a website
driver.get("https://www.google.ca/")

#What this does is it uses our webdriver, waits 5 seconds for the UI to fully load in
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

#find the element, in this case it's the search space in google
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
#this basically clears any elements in the search space if it came preoccupied 
input_element.clear()

#enter in "Selenium Tools in the search space"
#Add in the Enter key 
input_element.send_keys("Selenium Tools" + Keys.ENTER)



#add delay to see what's going on
time.sleep(10)

driver.quit()