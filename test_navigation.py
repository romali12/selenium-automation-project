import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_navigation_and_element_verification():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    driver.get("https://automationexercise.com")

    #verify home page title
    assert "Automation Exercise" in driver.title

    #click on sign up/login link
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(2)

    #verify URL and login elements
    assert "login" in driver.current_url
    assert driver.find_element(By.NAME, "email")
    assert driver.find_element(By.NAME, "password")

    # go back to homepage
    driver.find_element(By.XPATH, "//img[@alt='Website for automation practice']").click()
    time.sleep(2)

    #click on test cases link
    driver.find_element(By.LINK_TEXT, "Test Cases").click()
    time.sleep(2)

    #click on products link
    driver.find_element(By.XPATH, "//a[@href='/products']").click()
    time.sleep(2)

    #click on API Testing link
    driver.find_element(By.LINK_TEXT, "API Testing").click()
    time.sleep(2)

    #click on Cart link
    driver.find_element(By.LINK_TEXT, "Cart").click()
    time.sleep(2)

    #click on video tutorial link
    driver.find_element(By.LINK_TEXT,"Video Tutorials").click()
    time.sleep(2)

    #navigate to contact us page
    driver.find_element(By.LINK_TEXT, "Contact us").click()
    time.sleep(2)

    #content form is visible
    assert driver.find_element(By.NAME, "name")
    assert driver.find_element(By.NAME, "email")
    assert driver.find_element(By.NAME, "message")
    driver.quit()
