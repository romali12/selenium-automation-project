import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_login_button_enabled():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://automationexercise.com")
    driver.maximize_window()
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
    assert login_button.is_enabled()
    driver.quit()
    time.sleep(3)
