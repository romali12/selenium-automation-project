import time

from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_first_product_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        time.sleep(3)

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(3)
