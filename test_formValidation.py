import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from HTMLProject.formValidation import submit_btn


@pytest.fixture
def driver():
    service_obj = Service("C:/Users/Dixit/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("file:///C:/Users/Dixit/PycharmProjects/PythonProject/HTMLProject/Form.html")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_empty_field(driver):
    submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_btn.click()
    time.sleep(3)

def test_field_active(driver):
    active_element = driver.switch_to.active_element
    active_element.get_attribute("placeholder")
    time.sleep(3)

def test_invalid_email(driver):
    submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    driver.find_element(By.ID,"name").send_keys("Test User")
    driver.find_element(By.ID,"email").send_keys("demo.gmail.com")
    driver.find_element(By.ID,"password").send_keys("abc@123")
    submit_btn.click()
    time.sleep(3)

def test_valid_input(driver):
    submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    driver.find_element(By.ID,"email").clear()
    driver.find_element(By.ID,"email").send_keys("demouser@gmail.com")
    submit_btn.click()
    time.sleep(3)

def test_valid_username(driver):
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    driver.find_element(By.ID,"name").send_keys("Test User")
    time.sleep(3)

print("Data Submitted Successfully..!!")
time.sleep(3)
