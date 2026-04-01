import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    yield driver
    driver.quit()

def test_login(driver):
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID,"submit").click()
    time.sleep(3)

    #Logout code here
    driver.find_element(By.LINK_TEXT, "Log out").click()
    time.sleep(3)
time.sleep(3)
