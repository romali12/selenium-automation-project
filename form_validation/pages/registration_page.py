from selenium.webdriver.common.by import By

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://demo.automationtesting.in/Register.html")

    def fill_form(self, first_name, last_name, email, phone):
        self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys(first_name)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys(last_name)
        self.driver.find_element(By.XPATH, "//input[@type='email']").send_keys(email)
        self.driver.find_element(By.XPATH, "//input[@type='tel']").send_keys(phone)

    def submit(self):
        self.driver.find_element(By.ID, "submitbtn").sclick()
