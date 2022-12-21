from getData import scrape
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Edge()

driver.get('https://www.espncricinfo.com/series/england-in-pakistan-2022-23-1330866/pakistan-vs-england-3rd-test-1330873/ball-by-ball-commentary')

time.sleep(1)
previousHeight = driver.execute_script('return document.body.scrollHeight;')
elements = []

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    # pageSource = driver.page_source
    deliveries = driver.find_elements(By.XPATH, "//*[@class='ds-text-tight-s ds-font-regular ds-mb-1 lg:ds-mb-0 lg:ds-mr-3 ds-block ds-text-center']")
    players = driver.find_elements(By.XPATH, "//*[@class='ds-leading-none ds-mb-0.5']")
    descriptions = driver.find_elements(By.XPATH, "//*[@class='ci-html-content']")
    # for element in elements3:
    #     print(element.text)
    time.sleep(1)

    newHeight = driver.execute_script('return document.body.scrollHeight;')
    if newHeight == previousHeight:
        for i in range(len(deliveries)):
            print(deliveries[i].text, players[i].text, descriptions[i].text, "\n")
        break

    previousHeight = newHeight

