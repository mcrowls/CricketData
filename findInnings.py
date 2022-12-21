from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from automateScrolling import scroller 
import time


def findDifferentInnings(path):
    driver = webdriver.Edge()
    driver.get(path)
    wait = WebDriverWait(driver,30)
    try:
        driver.execute_script("window.scrollBy(0,50);")
        wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='onetrust-accept-btn-handler']"))).click()
    except:
        print("No Cookie Adds")
    pagination = wait.until(EC.element_to_be_clickable((By.XPATH,"//i[@class='icon-keyboard_arrow_down-outlined ds-text-icon-primary ds-ml-2 ds-ml-auto']")))
    pagination.click()
    elements = driver.find_elements(By.XPATH,"//span[@class='ds-grow']")
    inns = []
    for el in elements:
        inns.append(el)
    return inns


def specificInnings(path, innings):
    driver = webdriver.Edge()
    driver.get(path)
    wait = WebDriverWait(driver,50)
    try:
        driver.execute_script("window.scrollBy(0,50);")
        wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='onetrust-accept-btn-handler']"))).click()
    except:
        print("No Cookie Adds")
    pagination = wait.until(EC.element_to_be_clickable((By.XPATH,"//i[@class='icon-keyboard_arrow_down-outlined ds-text-icon-primary ds-ml-2 ds-ml-auto']")))
    pagination.click()
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='No thanks']"))).click()
    except:
        print("No pop ups")
    option = wait.until(EC.element_to_be_clickable(innings))
    option.click()
    x, y, z = scroller(driver)
    return x, y, z


innings = findDifferentInnings('https://www.espncricinfo.com/series/england-in-pakistan-2022-23-1330866/pakistan-vs-england-3rd-test-1330873/ball-by-ball-commentary')

for i in range(len(innings)):
    inn1, inn2, inn3 = specificInnings('https://www.espncricinfo.com/series/england-in-pakistan-2022-23-1330866/pakistan-vs-england-3rd-test-1330873/ball-by-ball-commentary', innings[i])


    print(inn2[-1])