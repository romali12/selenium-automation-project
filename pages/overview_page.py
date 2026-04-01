import time

from selenium.webdriver.common.by import By

class OverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def click_finish(self):
        self.driver.find_element(By.ID, "finish").click()
        time.sleep(3)
