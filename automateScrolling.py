from getData import group
from selenium import webdriver
import numpy as np
from selenium.webdriver.common.by import By
import time



def scroller(path):
    driver = webdriver.Edge()
    driver.get(path)
    time.sleep(1)
    previousHeight = driver.execute_script('return document.body.scrollHeight;')
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        deliveries = driver.find_elements(By.XPATH, "//*[@class='ds-text-tight-s ds-font-regular ds-mb-1 lg:ds-mb-0 lg:ds-mr-3 ds-block ds-text-center']")
        players = driver.find_elements(By.XPATH, "//*[@class='ds-leading-none ds-mb-0.5']")
        descriptions = driver.find_elements(By.XPATH, "//*[@class='ci-html-content']")
        time.sleep(1)
        newHeight = driver.execute_script('return document.body.scrollHeight;')
        if newHeight == previousHeight:
            deliveriesArr = []
            playersArr = []
            descriptionsArr = []
            for i in range(len(deliveries)):
                if deliveries[i].text not in deliveriesArr:
                    deliveriesArr.append(deliveries[i].text)
            for i in range(len(players)):
                playersArr.append(players[i].text)
            for i in range(len(descriptions)):
                if descriptions[i].text not in descriptionsArr:
                    descriptionsArr.append(descriptions[i].text)
            break
        previousHeight = newHeight
    return deliveriesArr, playersArr, descriptionsArr 



d, p, des = scroller('https://www.espncricinfo.com/series/england-in-pakistan-2022-23-1330866/pakistan-vs-england-3rd-test-1330873/ball-by-ball-commentary')

arrs = group(d, p, des)

print(arrs)




