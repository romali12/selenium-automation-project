import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://sandbox.myshopify.com/")
    yield driver
    driver.quit()

def test_search_product(driver):
    #search product to search bar
    search = driver.find_element(By.NAME,"q")
    search.send_keys("t-shirt")
    search.send_keys(Keys.ENTER)
    time.sleep(2)

    #click on product link
    driver.find_element(By.LINK_TEXT,"Shopify T-Shirt").click()
    time.sleep(2)

    #click on add to cart button
    driver.find_element(By.ID,"add").click()
    time.sleep(2)
