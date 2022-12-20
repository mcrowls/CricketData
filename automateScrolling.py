from getData import scrape
from bs4 import BeautifulSoup
from selenium import webdriver
import time


driver = webdriver.Edge()

driver.get('https://www.espncricinfo.com/series/england-in-pakistan-2022-23-1330866/pakistan-vs-england-3rd-test-1330873/ball-by-ball-commentary')

time.sleep(3)
previousHeight = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    pageSource = driver.page_source
    arr = scrape(pageSource)
    time.sleep(5)

    newHeight = driver.execute_script('return document.body.scrollHeight')
    if newHeight == previousHeight:
        break

    previousHeight = newHeight
