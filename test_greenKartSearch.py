import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    yield driver
    driver.quit()


def test_search_product_keyword(driver):
    wait = WebDriverWait(driver, 15)

    # Search product
    search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-keyword")))
    search_box.send_keys("ca")

    # Wait for products to load
    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='products']/div")))

    # Add all products to cart (stale-element safe)
    products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
    for i in range(len(products)):
        retry = 0
        while retry < 3:
            try:
                buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
                wait.until(EC.element_to_be_clickable(buttons[i])).click()
                break
            except StaleElementReferenceException:
                retry += 1

    # Open cart
    wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Cart']"))).click()

    # Proceed to checkout
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='PROCEED TO CHECKOUT']"))).click()

    # Enter promo code
    promo_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".promoCode")))
    promo_input.send_keys("rahulshettyacademy")

    # Apply promo code
    driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

    # Wait for promo confirmation
    promo_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".promoInfo"))).text
    print("Promo message:", promo_text)

    # Place order
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']"))).click()

    # Select country
    country_dropdown = wait.until(EC.presence_of_element_located((By.TAG_NAME, "select")))
    Select(country_dropdown).select_by_visible_text("India")

    # Agree terms
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".chkAgree"))).click()

    # Proceed
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Proceed']"))).click()
    