import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.wikipedia.org/")
    yield driver
    driver.quit()

def test_search_valid(driver):
    driver.find_element(By.ID,"searchInput").send_keys("python")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

def test_search_invalid(driver):
    driver.find_element(By.ID, "searchInput").send_keys("sdfdfdsfdsf")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    driver.implicitly_wait(5)
    time.sleep(3)
time.sleep(3)
