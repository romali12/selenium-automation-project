import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:/Users/Dixit/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://testpages.herokuapp.com/styled/basic-html-form-test.html")
driver.maximize_window()

def test_form():
    driver.find_element(By.NAME, "username").send_keys("Test")
    driver.find_element(By.NAME, "password").send_keys("Pass123")
    driver.find_element(By.XPATH, "//textarea[@name='comments']").send_keys("Something new...")
    driver.find_element(By.NAME, "filename").send_keys("C:/Users/Dixit/Downloads/female-avatar.png")
    driver.find_element(By.XPATH, "//input[@value='cb3']").click()
    driver.find_element(By.XPATH, "//input[@value='rd1']").click()
    multi_select = Select(driver.find_element(By.NAME, "multipleselect[]"))
    multi_select.select_by_visible_text("Selection Item 1")
    multi_select.select_by_visible_text("Selection Item 2")
    driver.find_element(By.XPATH,"//option[@value='dd2']").click()
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    time.sleep(3)
