import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, \
    TimeoutException


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless=new")  # Jenkins-friendly
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    yield driver
    driver.quit()


def test_search_product_keyword(driver):
    wait = WebDriverWait(driver, 20)

    # Search product
    search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-keyword")))
    search_box.send_keys("ca")

    # Wait until products appear
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products .product")))

    # Add all products to cart (dynamic iteration, safe for headless)
    while True:
        try:
            # Fetch visible "Add to Cart" buttons dynamically
            buttons = driver.find_elements(By.CSS_SELECTOR, ".product-action button")
            if not buttons:
                break  # No more buttons to click
            for button in buttons:
                try:
                    wait.until(EC.element_to_be_clickable(button)).click()
                except (StaleElementReferenceException, ElementClickInterceptedException):
                    continue
            break  # Exit after clicking all buttons
        except TimeoutException:
            break

    # Open cart
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt='Cart']"))).click()

    # Proceed to checkout
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='PROCEED TO CHECKOUT']"))).click()

    # Enter promo code
    promo_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".promoCode")))
    promo_input.send_keys("rahulshettyacademy")
    driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

    # Wait for promo confirmation
    promo_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".promoInfo"))).text
    print("Promo message:", promo_text)

    # Place order
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']"))).click()

    # Select country
    country_dropdown = wait.until(EC.presence_of_element_located((By.TAG_NAME, "select")))
    Select(country_dropdown).select_by_visible_text("India")

    # Agree terms and proceed
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".chkAgree"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Proceed']"))).click()

    print("✅ Test completed successfully!")
