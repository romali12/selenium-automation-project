import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    yield driver
    driver.quit()

def test_e2e(driver):
    # Click on "Shop" link
    driver.find_element(By.LINK_TEXT, "Shop").click()
    time.sleep(5)

    # Get all product cards
    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    time.sleep(5)

    # Loop through each product and add 'Blackberry' to cart
    for product in products:
        product_name = product.find_element(By.XPATH, "div/h4/a").text
        if product_name == "Blackberry":
            product.find_element(By.XPATH, "div/button").click()
            break
        time.sleep(5)

    # Add to Cart
    driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    time.sleep(5)

    # Checkout Button
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    time.sleep(5)

    driver.find_element(By.ID, "country").send_keys("ind")
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "India"))
    )

    # Then find and click 'India'
    countries = driver.find_elements(By.CSS_SELECTOR, "ul li a")
    for country in countries:
        if country.text.strip() == "India":
            country.click()
            break
    assert driver.find_element(By.ID, "country").get_attribute("value") == "India"
    time.sleep(5)

    # Click Checkbox
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

    # Submit Button
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # Success message
    successText = driver.find_element(By.CLASS_NAME, "alert-success").text
    time.sleep(5)
