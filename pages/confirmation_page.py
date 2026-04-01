from selenium.webdriver.common.by import By

class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver

    def get_confirmation_message(self):
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text
