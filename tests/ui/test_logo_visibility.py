from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_logo_visibility():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://automationexercise.com")
    driver.maximize_window()
    logo = driver.find_element(By.XPATH, "//img[@alt='Website for automation practice']")
    assert logo.is_displayed()
    driver.quit()
