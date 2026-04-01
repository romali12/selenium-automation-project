import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("file:///C:/Users/Dixit/PycharmProjects/PythonProject/HTMLProject/login.html")
    yield driver
    driver.quit()

#Test case for Valid Login
def test_valid_login(driver):
    driver.find_element(By.ID,"username").send_keys("testuser")
    driver.find_element(By.ID,"password").send_keys("user@098")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    #assert "dashboard" in driver.current_url.lower() or "Welcome" in driver.page_source

#Test case for InValid Login
def test_invalid_login(driver):
    driver.find_element(By.ID, "username").send_keys("user")
    driver.find_element(By.ID, "password").send_keys("user123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
