import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SliderPage:
    NEXT_ARROW = (By.CSS_SELECTOR, ".slick-arrow.slick-next")
    ACTIVE_SLIDE_IMG = (By.CSS_SELECTOR, ".slick-slide.slick-active img")
    ALL_SLIDE_IMGS = (By.CSS_SELECTOR, ".slick-slide img")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def scroll_to_slider(self):
        slider_elem = self.wait.until(
            EC.presence_of_element_located(self.ACTIVE_SLIDE_IMG)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            slider_elem
        )
        time.sleep(1)

    def get_active_slide_src(self):
        img = self.wait.until(
            EC.visibility_of_element_located(self.ACTIVE_SLIDE_IMG)
        )
        time.sleep(1)
        return img.get_attribute("src")

    def click_next(self):
        next_arrow = self.wait.until(EC.element_to_be_clickable(self.NEXT_ARROW))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_arrow)
        time.sleep(1)
        next_arrow.click()
        self.wait.until(EC.visibility_of_element_located(self.ACTIVE_SLIDE_IMG))

    def get_unique_slide_count(self):
        imgs = self.driver.find_elements(*self.ALL_SLIDE_IMGS)
        return len(set([img.get_attribute("src") for img in imgs if img.get_attribute("src")]))
