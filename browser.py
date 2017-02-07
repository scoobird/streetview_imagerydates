from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import json
import re

"""
gotoAddress fetches google map of address,
clicksthrough to streetview,
grabs timestamp

browser hella timeout-prone
"""
def gotoAddress(url):
    driver.get(url)
    try:
        element = WebDriverWait(driver, 75).until(
            EC.presence_of_element_located((
                By.XPATH, "//*[@id=\"pane\"]/div/div[2]/div/div/div[6]/div[1]/button"
                ))
            )
        element.click()
        try:
            timestamp = WebDriverWait(driver, 75).until(
                EC.presence_of_element_located((
                    By.XPATH, "//*[@id=\"titlecard\"]/div[1]/div[2]/div[4]/div/div"
                    ))
                )
            streetviewdate = timestamp.text
            print(streetviewdate) #store this

        finally: print("streetview request completed")
        
    finally:
        print("visited " + url)
        driver.quit()
   
"""
selenium, initiate browser
"""
chromedriver = "C:\Program Files (x86)\Google\Chrome\chromedriver"
driver = webdriver.Chrome(chromedriver)
# begin loop over address objects
address = "6221+Osage+Ave,+Philadelphia,+PA+19143" #test value replace w/ addr object
url = "https://www.google.com/maps/place/"+address
gotoAddress(url)

