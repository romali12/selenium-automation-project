import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    service_obj = Service("C:/Users/Dixit/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("file:///C:/Users/Dixit/PycharmProjects/PythonProject/pytestDemo/job_application.html")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_job_application(driver):

    #Enter FullName
    fullName = driver.find_element(By.ID, "fullname")
    fullName.send_keys("Shloka Patel")
    time.sleep(2)

    #Enter Email Address
    email = driver.find_element(By.XPATH, "//input[@type='email']")
    email.send_keys("abc@gmail.com")
    time.sleep(2)

    #Enter Phone number
    phoneNum = driver.find_element(By.ID, "phone")
    phoneNum.send_keys("8754102130")
    time.sleep(2)

    #Select position
    position_dropdown = Select(driver.find_element("xpath", "//select[@id='position']"))
    position_dropdown.select_by_visible_text("QA Tester")
    time.sleep(2)

    #Upload resume
    upload_resume = driver.find_element("xpath", "//input[@id='resume']")
    upload_resume.send_keys("C:/Users/Dixit/Downloads/Hf-Sphurti.pdf")
    time.sleep(2)

    #submit application
    submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()
    time.sleep(3)
