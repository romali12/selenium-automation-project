import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    service_obj = Service("C:/Users/Dixit/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_inputs(driver):
    wait = WebDriverWait(driver, 5)

    user_name = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    user_name.send_keys("Admin")
    time.sleep(3)

    password = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    password.send_keys("admin123")
    time.sleep(3)

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()
    time.sleep(3)

    dashboard = wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
    assert dashboard.is_displayed()
    time.sleep(5)

def test_invalid_inputs(driver):
    wait = WebDriverWait(driver, 5)

    us_name = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    us_name.send_keys("admin")
    time.sleep(3)

    pass_word = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    pass_word.send_keys("Admin1234")
    time.sleep(3)

    login = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login.click()
    time.sleep(3)

def test_username_incorrect(driver):
    wait = WebDriverWait(driver, 5)
    username = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    username.send_keys("test")
    time.sleep(3)

    pass_key = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    pass_key.send_keys("admin123")
    time.sleep(3)

    login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_btn.click()
    time.sleep(3)
