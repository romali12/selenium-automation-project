import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Setup driver
def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)

def test_travel_booking():
    driver = create_driver()
    driver.maximize_window()
    driver.get("https://www.phptravels.net/")

    #click on flight tab
    driver.find_element(By.XPATH, "//li[@class='nav-item']//button[span[text()='Flights']]").click()
    time.sleep(3)

    #enter from city
    city_from = driver.find_element(By.XPATH, "//input[@name='from' and @placeholder='Flying From']")
    city_from.send_keys("ZLS - Liverpool Street Station")
    time.sleep(2)
    city_from.send_keys(Keys.ENTER)
    time.sleep(3)

    #enter to city
    city_to = driver.find_element(By.XPATH, "//input[@name='to' and @placeholder='Flying From']")
    city_to.send_keys("HKT - Phuket International Airport")
    time.sleep(2)
    city_to.send_keys(Keys.ENTER)
    time.sleep(3)

    #click departure date
    calendar = driver.find_element(By.ID, "departure")
    calendar.clear()
    time.sleep(2)
    calendar.click()
    calendar.send_keys("10-08-2025")
    calendar.click()
    time.sleep(3)

    # Click search
    driver.find_element(By.XPATH, "//button[@id='flights-search']").click()
    time.sleep(5)

    # Verify result text
    results = driver.find_elements(By.XPATH, "//div[contains(@class, 'flight-card')]")
    if results:
        print("Flights search results displayed successfully.")
    else:
        print("No flights found or search failed.")

    driver.quit()
