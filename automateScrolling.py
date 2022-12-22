from getData import group
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def scroller(driver):
    previousHeight = driver.execute_script('return document.body.scrollHeight;')
    wait = WebDriverWait(driver,2)
    time.sleep(1)
    iterator = 1
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        deliveries = driver.find_elements(By.XPATH, "//*[@class='ds-text-tight-s ds-font-regular ds-mb-1 lg:ds-mb-0 lg:ds-mr-3 ds-block ds-text-center']")
        players = driver.find_elements(By.XPATH, "//*[@class='ds-leading-none ds-mb-0.5']")
        descriptions = driver.find_elements(By.XPATH, "//*[@class='ci-html-content']")
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='No thanks']"))).click()
        except:
            continue
        time.sleep(5)
        newHeight = driver.execute_script('return document.body.scrollHeight;')
        if newHeight == previousHeight:
            print("yes")
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
        iterator += 1
    return deliveriesArr, playersArr, descriptionsArr 



# d, p, des = scroller('https://www.espncricinfo.com/series/england-in-pakistan-2022-23-1330866/pakistan-vs-england-3rd-test-1330873/ball-by-ball-commentary')

# arrs = group(d, p, des)

# for arr in arrs:
#     print(arr.__dict__)

# print(arrs)

# differentInnings('https://www.espncricinfo.com/series/england-in-pakistan-2022-23-1330866/pakistan-vs-england-3rd-test-1330873/ball-by-ball-commentary')




