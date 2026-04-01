import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASEURL = "https://hf.redliodesigns.com/products"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_filtter(driver):
    driver.get(BASEURL)
    driver.find_element(By.ID,"animal-goat").click()
    time.sleep(2)
    driver.find_element(By.ID,"animal-bull").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[text()='Clear All']").click()
    time.sleep(2)

def test_product_click(driver):
    driver.get(BASEURL)

    product_xpath = "//a[@href='/products/kanak-senior']"
    product_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, product_xpath))
    )
    product_element.click()
    WebDriverWait(driver, 10).until(
        lambda d: "/products/kanak-senior" in d.current_url
    )
    assert "/products/kanak-senior" in driver.current_url
    time.sleep(3)
    