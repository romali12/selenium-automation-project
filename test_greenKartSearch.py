import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


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
    results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='products']/div")))
    print(f"Number of results found: {len(results)}")
    assert len(results) > 0

    # Add all products to cart
    for result in results:
        result.find_element(By.XPATH, "div/button").click()

    # Open cart
    wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='Cart']"))).click()

    # Proceed to checkout
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='PROCEED TO CHECKOUT']"))).click()

    # Enter promo code
    promo_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".promoCode")))
    promo_input.send_keys("rahulshettyacademy")

    # Apply promo code
    driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

    # Wait for promo confirmation (IMPORTANT FIX)
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