from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def differentInnings(path):
    driver = webdriver.Edge()
    driver.get(path)
    wait = WebDriverWait(driver,30)
    try:
        # Close the footer add
        wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@id='ezmob-wrapper']/div/center/span/div/div/span"))).click()
        # Scroll a distance so that the Cookie pop up appears and Close it
        driver.execute_script("window.scrollBy(0,50);")
        wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='rcc-confirm-button']"))).click()
    except:
        print("no adds")
    time.sleep(1)
    return