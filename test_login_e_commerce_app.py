import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    service_obj = Service("C:/Users/Dixit/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://magento.softwaretestingboard.com/customer/account/login/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    driver.find_element(By.ID, "email").send_keys("patil098@gmail.com")
    driver.find_element(By.ID, "pass").send_keys("admin@123")
    driver.find_element(By.ID, "send2").click()
    time.sleep(3)

    logo = driver.find_element(By.XPATH, "//a[@class='logo']//img[@alt='']")
    logo.click()
    time.sleep(3)
