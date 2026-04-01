import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_magento_add_and_remove_from_cart(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://magento.softwaretestingboard.com/")

    #search for product
    search = driver.find_element(By.ID, "search")
    search.send_keys("Juno Jacket")
    search.send_keys(Keys.ENTER)
    time.sleep(2)

    #click the product
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Juno Jacket"))).click()
    time.sleep(2)

    #select size and color
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.swatch-attribute.size div.swatch-option"))).click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.swatch-attribute.color div.swatch-option"))).click()
    time.sleep(2)

    #click add to cart
    add_button = wait.until(EC.element_to_be_clickable((By.ID, "product-addtocart-button")))
    add_button.click()
    time.sleep(2)

    #wait for success message or mini cart update
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "message-success")))
    time.sleep(2)
    
    #go to cart
    driver.get("https://magento.softwaretestingboard.com/checkout/cart/")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart.item")))
    time.sleep(2)

    #assert item is in cart
    cart_items = driver.find_elements(By.CSS_SELECTOR, ".cart.item")
    assert len(cart_items) > 0, "Cart is empty!"
    time.sleep(2)

    #remove from cart
    driver.find_element(By.CSS_SELECTOR, "a.action.action-delete").click()
    time.sleep(2)

    #assert cart is now empty
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-empty")))
    empty_message = driver.find_element(By.CSS_SELECTOR, ".cart-empty").text
    assert "You have no items in your shopping cart" in empty_message
    time.sleep(2)
