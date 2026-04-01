import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.myntra.com/")
    yield driver
    driver.quit()

def test_product_search(driver):
    #Search product using keyword
    search_box = driver.find_element(By.CLASS_NAME, "desktop-searchBar")
    search_box.send_keys("Kurties")
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    #Brand Filtering
    brand_filter = driver.find_elements(By.CSS_SELECTOR,"ul.brand-list li label")
    for filter_item  in brand_filter:
        if "KALINI" in filter_item .text:
            filter_item .click()
            time.sleep(2)

    #Scroll to price filter section
    price_filter = driver.find_element(By.XPATH, "//span[text()='Price']")
    driver.execute_script("arguments[0].scrollIntoView();", price_filter)
    time.sleep(2)
    left_slider = driver.find_element(By.ID, "rootRailThumbLeft")
    right_slider = driver.find_element(By.ID, "rootRailThumbRight")
    action = ActionChains(driver)
    action.click_and_hold(right_slider).move_by_offset(-160, 0).release().perform()
    time.sleep(2)

    #Verify display price range
    price_range = driver.find_element(By.CLASS_NAME, "slider-dotContainer").text
    print(f"Price range selected: {price_range}")
    time.sleep(2)

    #Color Filtering
    color_select = ["Green","Pink"]
    color_filter = driver.find_elements(By.CSS_SELECTOR, "li.colour-listItem label")
    for colortext in color_filter:
        color_Text = colortext.text.split('(')[0].strip()
        if color_Text in color_select:
            driver.execute_script("arguments[0].click();", colortext)
            time.sleep(2)

    #Discount Range filtering
    range_filter = driver.find_elements(By.CSS_SELECTOR,"ul.discount-list li label")
    for diss_filter in range_filter:
        if "50% and above" in diss_filter.text:
            diss_filter.click()
            time.sleep(2)

    #click on sorting dropdown
    sort_dropdown = driver.find_element(By.CSS_SELECTOR, ".sort-downArrow")
    driver.execute_script("arguments[0].click();", sort_dropdown)
    time.sleep(3)

    #Select "Customer Rating"
    sort_option = driver.find_element(By.XPATH, "//label[contains(., 'Customer Rating')]")
    driver.execute_script("arguments[0].click();", sort_option)
    time.sleep(3)

    #Clear all link filtering
    try:
        clearAll = driver.find_element(By.XPATH, "//span[text()='CLEAR ALL']")
        clearAll.click()
        print("'CLEAR ALL' clicked.")
        # Wait and refresh the page
        time.sleep(2)
    except Exception as e:
        print("Could not click 'CLEAR ALL':", e)
    time.sleep(2)
time.sleep(3)
