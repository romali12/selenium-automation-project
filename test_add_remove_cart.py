import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automationteststore.com/")
    yield driver
    driver.quit()

def test_add_remove_cart(driver):
    search = driver.find_element(By.ID, "filter_keyword")
    search.send_keys("skincare")
    search.send_keys(Keys.ENTER)
    time.sleep(2)

    #Update Quantity
    qty = driver.find_element(By.ID, "product_quantity")
    qty.clear()
    qty.send_keys("3")
    time.sleep(2)

    #Add to cart button
    button = (driver.find_element(By.CSS_SELECTOR,"ul.productpagecart a.cart"))
    button.click()
    time.sleep(2)

    #Remove(Delete) product from checkout
    #driver.find_element(By.CSS_SELECTOR,".btn-sm").click()
    #time.sleep(2)

    #Qty Update from checkout page
    qty_update = driver.find_element(By.ID,"cart_quantity96")
    qty_update.clear()
    qty_update.send_keys("2")

    update_cart = driver.find_element(By.ID, "cart_update")
    update_cart.click()
    time.sleep(2)

    #Checkout button
    driver.find_element(By.LINK_TEXT,"Checkout").click()
    time.sleep(2)
time.sleep(2)
