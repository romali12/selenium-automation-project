import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://hf.redliodesigns.com/"

@pytest.mark.usefixtures("driver")
class TestNavigation:

    def test_logo_visibility(self, driver):
        driver.get(BASE_URL)
        logo = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='Hindustan Feeds']"))
        )
        assert logo.is_displayed(), "Logo is not visible."
        time.sleep(3)

    #def test_navigation_links_clickable(self, driver):
    #    driver.get(BASE_URL)
     #   nav_links = WebDriverWait(driver, 10).until(
      #      EC.presence_of_all_elements_located((By.CSS_SELECTOR, "nav a"))
       # )

        #for i in range(len(nav_links)):
         #   driver.get(BASE_URL)  # reset page each time
          #  nav_links = WebDriverWait(driver, 10).until(
           #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "nav a"))
            #)
            #link = nav_links[i]
            #href = link.get_attribute("href")
            #driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", link)
            #WebDriverWait(driver, 5).until(EC.element_to_be_clickable(link))
            #old_url = driver.current_url
            #link.click()

            #if href != old_url:
             #   WebDriverWait(driver, 10).until(EC.url_changes(old_url))
              #  assert driver.current_url == href, f"Click on {href} did not navigate correctly."
           # else:
            #    time.sleep(1)
            #time.sleep(3)

    def test_navigation_spacing(self, driver):
        driver.get(BASE_URL)
        nav_items = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "nav a"))
        )
        assert len(nav_items) > 1, "Navigation items not found"

        for i in range(len(nav_items) - 1):
            first = nav_items[i].rect
            second = nav_items[i + 1].rect
            spacing = second['x'] - (first['x'] + first['width'])

            assert math.isclose(spacing, 30, abs_tol=0.5), \
                f"Spacing between item {i} and {i + 1} is {spacing}px, expected ~30px"
        time.sleep(3)

    def test_explore_product(self, driver):
        driver.get(BASE_URL)
        click_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Explore Our Products']"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", click_btn)
        time.sleep(2)
        driver.execute_script("arguments[0].click();", click_btn)
        WebDriverWait(driver, 5).until(EC.url_contains("/products"))
        time.sleep(3)

    def test_contact_click(self, driver):
        driver.get(BASE_URL)
        contact_click = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Contact Us']"))
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", contact_click)
        time.sleep(2)
        driver.execute_script("arguments[0].click();", contact_click)
        WebDriverWait(driver, 5).until(EC.url_contains("/contact"))
        time.sleep(3)

    def test_our_products(self, driver):
        driver.get(BASE_URL)
        our_product = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[span[text()='Cow Feed']]"))
        )
        time.sleep(2)
        driver.execute_script("arguments[0].click();", our_product)
        time.sleep(3)

        btn_click = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='View All' and contains(@href,'filter=cow')]"))
        )
        btn_click.click()
        time.sleep(3)

    def test_click_accordions(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        first_accordion = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Trusted by Farmers for Over 35 Years']")
        ))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_accordion)
        first_accordion.click()
        wait.until(EC.visibility_of_element_located((
            By.XPATH,
            "//div[contains(@class,'accordion-body') and contains(text(),\"Our legacy is built\")]"
        )))
        time.sleep(2)

        second_accordion = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//button[normalize-space()='Scientifically Formulated Nutrition']"
        )))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", second_accordion)
        second_accordion.click()
        time.sleep(2)

        third_accordion = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//button[normalize-space()='State-of-the-Art Manufacturing']"
        )))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", third_accordion)
        third_accordion.click()
        time.sleep(2)

        four_accordion = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            "//button[normalize-space()='Wide Dealer & Delivery Network']"
        )))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", four_accordion)
        four_accordion.click()
        time.sleep(2)
    