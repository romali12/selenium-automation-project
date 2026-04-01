import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# ===== CONFIG =====
CHROME_DRIVER_PATH = "C:/Users/Dixit/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
BASE_URL = "https://demo-m2.bird.eu/"
PASSWORD = "Admin@123"
SEARCH_KEYWORD = "bag"

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, 20)    
actions = ActionChains(driver)

try:
    driver.get(BASE_URL)

    account_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".customer-welcome")))
    actions.move_to_element(account_icon).perform()
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Create an Account"))).click()

    wait.until(EC.visibility_of_element_located((By.ID, "firstname"))).send_keys("Romali")
    driver.find_element(By.ID, "lastname").send_keys("Patil")
    unique_email = f"romali{int(time.time())}@gmail.com"
    driver.find_element(By.ID, "email_address").send_keys(unique_email)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "password-confirmation").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[span[text()='Create an Account']]").click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//h1/span[text()='My Account']")))
    print("Account created successfully")

    driver.find_element(By.CSS_SELECTOR, "a.logo").click()

    search_box = wait.until(EC.visibility_of_element_located((By.ID, "search")))
    search_box.clear()
    search_box.send_keys(SEARCH_KEYWORD)
    search_box.send_keys(Keys.RETURN)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-item-link"))).click()

    wait.until(EC.element_to_be_clickable((By.ID, "product-addtocart-button"))).click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".message-success"), "You added"))
    print("Product added to cart")

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".showcart"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "top-cart-btn-checkout"))).click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Shipping Address']")))
    print("Reached checkout page")

    time.sleep(3)

except Exception as e:
    print("Test Failed:", e)

finally:
    driver.quit()
