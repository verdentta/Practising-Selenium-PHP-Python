#import selenium
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 

#this package will help us to search stuff in html
from selenium.webdriver.common.by import By 

#this package will help us to type keys
from selenium.webdriver.common.keys import Keys 

#this package will help us with adding a wait for UI to load
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#to add a bit of delay to see what's happening :)
import time 

#let's initalize the webdriver 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

#let's go to a website
driver.get("https://books.toscrape.com/")

#wait till all elements are loaded in
WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.LINK_TEXT, "Psychology"))
)

time.sleep(3)

#go to the pyschology section
input_elem = driver.find_element(By.LINK_TEXT, "Psychology")
input_elem.click()


time.sleep(3)

#go to the music section
input_elem = driver.find_element(By.LINK_TEXT, "Music")
input_elem.click()

time.sleep(3)

#go to the fantasy section
input_elem = driver.find_element(By.LINK_TEXT, "Fantasy")
input_elem.click()


time.sleep(3)

#go back to the home section
input_elem = driver.find_element(By.LINK_TEXT, "Home")
input_elem.click()

time.sleep(5)



driver.quit()