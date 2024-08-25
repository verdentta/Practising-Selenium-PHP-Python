from selenium import webdriver
from selenium.webdriver.chrome.service import Service 

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time 

service = Service(executable_path = "chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://books.toscrape.com/")

time.sleep(3)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.LINK_TEXT, "A Light in the ..."))
)


input_element = driver.find_element(By.LINK_TEXT, "A Light in the ...")
input_element.click()

time.sleep(5)

driver.quit()