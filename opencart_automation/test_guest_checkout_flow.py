import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_guest_checkout(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.automationteststore.com/")

    #search for product
    search_box = driver.find_element(By.ID, "filter_keyword")
    search_box.send_keys("makeup")
    search_box.send_keys(Keys.ENTER)

    #click first product
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".fixed_wrapper .prdocutname"))).click()

    #click add to cart
    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='cart']"))).click()
    time.sleep(2)

    #go to cart
    driver.find_element(By.CSS_SELECTOR, "#cart_checkout1").click()

    #proceed as guest
    wait.until(EC.presence_of_element_located((By.ID, "guestFrm_firstname"))).send_keys("John")
    driver.find_element(By.ID, "guestFrm_lastname").send_keys("Doe")
    driver.find_element(By.ID, "guestFrm_email").send_keys("john.doe@example.com")
    driver.find_element(By.ID, "guestFrm_address_1").send_keys("123 Demo Street")
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.XPATH, "//button[@title='Continue']").click()
    print("Guest checkout filled successfully.")
    time.sleep(2)
