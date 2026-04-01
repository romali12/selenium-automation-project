import time
import csv
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Load CSV data
def read_test_data():
    with open('credentials.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [(row['username'], row['password'], row['expected_result']) for row in reader]

@pytest.mark.parametrize("username, password, expected_result", read_test_data())
def test_login(username, password, expected_result):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()

    if expected_result == "Valid":
        assert "Logged In Successfully" in driver.page_source
    else:
        assert "Your username is invalid!" in driver.page_source or \
               "Your password is invalid!" in driver.page_source
    time.sleep(3)
    driver.quit()
