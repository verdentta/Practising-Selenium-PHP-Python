#import pandas for data manipulation
import pandas as pd

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
driver.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")

#delay to load all elements in
time.sleep(5)

title_list = []
year_list=[]
rating_list=[]
edited_title_list=[]

#method to remove numbers from the movie titles
def remove_digits(strings):
    def is_alpha(char):
        return char.isalpha()
    return [''.join(filter(is_alpha, string)) for string in strings]

#set flag
flag = 0
#grab each movie title name 
while flag == 0:
    titles = driver.find_elements(By.CLASS_NAME, "ipc-metadata-list-summary-item__tc")
    for title in titles:
        
        movie_title = title.find_element(By.CLASS_NAME, "ipc-title__text").text
        #this returns a list of 3 different items since they all share the same class, it represents year, movie length and rating
        #but you only want the year so choose the first item
        movie_year = title.find_element(By.CSS_SELECTOR, "div.sc-b189961a-7.btCcOY.cli-title-metadata span:nth-child(1)").text
        movie_rating = title.find_element(By.CLASS_NAME, "ipc-rating-star--rating").text

        #add it to the lists
        title_list.append(movie_title)
        year_list.append(movie_year)
        rating_list.append(movie_rating)
        
    
    flag = 1

#remove the numbers from the movie titles
for title in title_list:
    title = title.split(". ", 1)[1]
    edited_title_list.append(title)

time.sleep(5) 
driver.quit()

#create the dataframe from the lists
df = pd.DataFrame({'Title': edited_title_list, 'Year': year_list, 'Rating': rating_list })

# Display the DataFrame
print(df)

#save it to a CSV file
df.to_csv('movie_dataset.csv', index=False)


#This script basically grabs data from the IMDB website top 250 movies, takes the title, year and rating and puts it into a CSV for 
#data alteration

