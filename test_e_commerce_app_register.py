import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    service_obj = Service("C:/Users/Dixit/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://demo-m2.bird.eu/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_resiter_user(driver):
    wait = WebDriverWait(driver, 3)

    # Click on Create an Account link
    create_acc_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Create an Account")))
    create_acc_link.click()
    time.sleep(2)

    # Fill in First Name
    firstName = wait.until(EC.presence_of_element_located((By.ID, "firstname")))
    firstName.send_keys("Romali")
    time.sleep(2)

    # Fill in Last Name
    lastName = driver.find_element(By.ID, "lastname")
    lastName.send_keys("Patil")
    time.sleep(2)

    #Click on checkbox
    checkbox = driver.find_element(By.ID, "assistance_allowed_checkbox")
    checkbox.click()
    time.sleep(2)

    # Fill in Email Address
    email_address = driver.find_element(By.ID, "email_address")
    email_address.send_keys("patil098@gmail.com")
    time.sleep(2)

    # Fill in Password
    password = driver.find_element(By.ID, "password")
    password.send_keys("admin@123")
    time.sleep(2)

    # Fill in Confirm Password
    confirmPass = driver.find_element(By.ID, "password-confirmation")
    confirmPass.send_keys("admin@123")
    time.sleep(2)

    #show password field
    driver.find_element(By.ID, "show-password").click()
    time.sleep(1)

    # Click Create an Account button
    create_button = driver.find_element(By.XPATH, "//button[span[text()='Create an Account']]")
    create_button.click()
    time.sleep(3)
