import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://hf.redliodesigns.com/about"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def get_active_slide_image(driver):
    active_slide = driver.find_element(By.CSS_SELECTOR, ".slick-slide.slick-active img")
    return active_slide.get_attribute("src")


def test_scroll_all_slides_multiple_times(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".slick-slide.slick-active")))
    next_arrow = driver.find_element(By.CSS_SELECTOR, ".slick-arrow.slick-next")
    loops = 2

    all_imgs = driver.find_elements(By.CSS_SELECTOR, ".slick-slide img")
    unique_images = list(set([img.get_attribute("src") for img in all_imgs]))
    total_slides = len(unique_images)

    print(f"Found {total_slides} unique slides")

    visited_slides = []
    for loop in range(loops):
        print(f"--- Loop {loop + 1} ---")
        for _ in range(total_slides):
            current_img = get_active_slide_image(driver)
            visited_slides.append(current_img)
            print(f"Slide: {current_img}")

            next_arrow.click()
            wait.until(lambda d: get_active_slide_image(d) != current_img)

            time.sleep(2)
    assert len(visited_slides) >= total_slides * loops, "Not all slides were visited"
    time.sleep(3)
