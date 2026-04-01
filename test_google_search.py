import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_google_search():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://gh-users-search.netlify.app/")

    seachBox = driver.find_element(By.XPATH, "//button[@type='submit']")
    seachBox.send_keys("Degreeck")
    time.sleep(3)
    seachBox.submit()
    time.sleep(5)
