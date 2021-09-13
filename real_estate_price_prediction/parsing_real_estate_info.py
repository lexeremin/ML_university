'''
TODO
Create parsing script to get selling real estatement ads data from craiglist sites(cian)

#1 find the way to get 50k+ link for individual ads

#2 open up every single link and get:
    -walk time to subway
    -adress(local area)
    -# of living rooms
    -size
    -floor
    -used or new
    -mb something else...

#3 make a pandas dataframe and write it to csv file
    
'''

from selenium import webdriver #tool for browser management
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup #used for html code parsing
import time
import csv
import datetime
#import pandas as pd 

#don't use it at all for now
flatten = lambda t: [item for sublist in t for item in sublist]

#get new links from the driver
def get_links(driver, distinct):
    link_stack = 0
    selling_apartment_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_93444fe79c--wrapper--E9jWb"))
    )
    #delete some shitty ads
    # elements = selling_apartment_list.find_elements_by_css_selector("li.product_item:not(.product_item--ad) a")
    elements = selling_apartment_list.find_elements_by_class_name("_93444fe79c--link--39cNw")
    #going to write results here
    filename = "test_cian_{}.txt".format(distinct)
    f = open(filename, "a")

    #write each link into the file 
    for element in elements:
        print(element.get_attribute("href"))
        link_stack += 1
        f.write(element.get_attribute("href")+'\n')
    #close file
    f.close()
    return link_stack

#webdriver setup path
DRIVER_PATH = '/Users/seeksub/Library/Mobile Documents/com~apple~CloudDocs/university/graduate degree/ML(Валиуллин)/продажа недвижимости/chromedriver'
#startup chrome
driver = webdriver.Chrome(DRIVER_PATH)

#setup height scroll for infinite scrolling
# last_height = driver.execute_script("return document.body.scrollHeight")

#distinct = 8
distincts = [1, 5, 6, 11, 4, 7, 10, 9, 8]
#try to fetch list(with size of more then 50k if possible) of selling apartments
links = 0
for distinct in distincts:
    page = 1
    try:
        while links<50001:
            #open irl
            irl = "https://www.cian.ru/cat.php?deal_type=sale&district%5B1%5D={}&engine_version=2&offer_type=flat&only_flat=1&region=1&room1=1&room2=1&room3=1&p={}&type=4".format(distinct,page)
            print(irl)
            driver.get(irl)
            #sleep to not get ban
            time.sleep(5)
            #read links and add number of added links
            links += get_links(driver, distinct)
            # links += 5000
            #get next page link and click it
            page+=1
        
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.LINK_TEXT, str(page)))
        # ).click()
        # print(next_page.get_attribute("href"))
        # if not next_page:
        #     print("no more pages left!")
        #     break
        # next_page.click()
            print("Page number:", page)
        # page +=1
            print("size:", links)
            if links < 1:
                break
        # break
        #END while   
    finally:
        #close chrome
        driver.quit()




# new real estate deals
#https://youla.ru/moskva/nedvijimost?attributes[sort_field]=date_published
#https://youla.ru/moskva/nedvijimost/prodaja-kvartiri
#/Users/seeksub/Library/Mobile Documents/com~apple~CloudDocs/university/graduate degree/ML(Валиуллин)/продажа недвижимости/chromedriver