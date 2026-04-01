import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def create_mobile_driver(device_name="iPhone X"):
    mobile_emulation = {"deviceName": device_name}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_argument("--disable-notifications")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def test_valid_login():
    driver = create_mobile_driver()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(3)
    assert "inventory" in driver.current_url
    print("Valid login passed.")
    time.sleep(3)
    driver.quit()

def test_invalid_login():
    driver = create_mobile_driver()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(3)
    error = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Username and password do not match" in error or "Epic sadface" in error
    print("Invalid login test passed.")
    time.sleep(3)
    driver.quit()

def test_empty_fields():
    driver = create_mobile_driver()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "login-button").click()
    time.sleep(3)
    error = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Username is required" in error
    print("Empty fields validation passed.")
    time.sleep(3)
    driver.quit()

if __name__ == "__main__":
    test_valid_login()
    test_invalid_login()
    test_empty_fields()
