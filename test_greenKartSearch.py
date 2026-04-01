import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.fixture
def driver():
    service_obj = Service("C:/Users/Dixit/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_search_product_keyword(driver):
    search_box = driver.find_element(By.CSS_SELECTOR, ".search-keyword")
    search_box.send_keys("ca")
    time.sleep(2)

    # Product match using this keyword
    results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
    count = len(results)
    print(f"Number of results found: {count}")
    assert count > 0
    for result in results:
        result.find_element(By.XPATH, "div/button").click()
    time.sleep(2)

    #Click mini cart
    driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
    time.sleep(2)

    #Click checkout button
    driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
    time.sleep(2)

    #Apply promocode
    driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
    time.sleep(2)

    #Click apply button
    driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
    print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
    time.sleep(2)

    #Click on place order button
    driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
    time.sleep(2)

    #Find the dropdown and select India
    Select(driver.find_element("tag name", "select")).select_by_visible_text("India")
    time.sleep(2)

    #Click checkbox
    driver.find_element(By.CSS_SELECTOR,".chkAgree").click()
    time.sleep(2)

    #Click proceed button
    driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
    time.sleep(2)
