import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

#browser setup
driver = webdriver.Chrome()
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()

def test_required_field_validation():
    try:
        #clear fields are filled
        driver.find_element(By.NAME, "firstname").clear()
        driver.find_element(By.NAME, "lastname").clear()
        time.sleep(2)

        #click submit
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)

        #check for alert popup (common in form validation)
        try:
            alert = driver.switch_to.alert
            print("Alert detected: ", alert.text)
            alert.accept()
        except NoAlertPresentException:
            print("No alert found. Check for inline validations.")

        #check if border color changes
        firstname_field = driver.find_element(By.NAME, "firstname")
        if firstname_field.get_attribute("required"):
            print("HTML5 'required' attribute present on firstname field.")
        else:
            print("No required attribute on firstname.")

    except Exception as e:
        print("Validation test failed:", str(e))
        time.sleep(2)

def test_positive_form_submission():
    try:
        #fill all fields
        driver.find_element(By.NAME, "firstname").send_keys("Alica")
        driver.find_element(By.NAME,"lastname").send_keys("Chetak")
        driver.find_element(By.ID,"sex-1").click()
        driver.find_element(By.ID,"exp-2").click()
        driver.find_element(By.ID,"datepicker").send_keys("15-07-1998")
        driver.find_element(By.ID,"profession-1").click()
        driver.find_element(By.ID, "tool-2").click()

        #continent dropdown
        Select(driver.find_element(By.ID, "continents")).select_by_visible_text("Asia")
        time.sleep(2)

        #selenium commands multiples select
        sel = Select(driver.find_element(By.ID, "selenium_commands"))
        sel.select_by_visible_text("Browser Commands")
        sel.select_by_visible_text("Navigation Commands")
        time.sleep(2)

        #submit form
        driver.find_element(By.ID, "submit").click()
        print("Form submitted successfully.")

    except Exception as e:
        print("Form submission failed:", str(e))
        time.sleep(2)

print("\n--- Running Negative Test Case (Required Fields) ---")
test_required_field_validation()

print("\n--- Running Positive Test Case (Successful Submission) ---")
test_positive_form_submission()

time.sleep(5)
driver.quit()
