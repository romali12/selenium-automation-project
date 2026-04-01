import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Import SliderPage from parent folder
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pytestDemo.hindustan_feed.slider_page import SliderPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    try:
        driver.quit()
    except:
        pass

def test_scroll_and_run_slider(driver):
    slider = SliderPage(driver)
    slider.open("https://hf.redliodesigns.com/become-a-dealer")
    slider.scroll_to_slider()

    total_slides = slider.get_unique_slide_count()
    loops = 2

    visited = []
    for loop in range(loops):
        print(f"--- Loop {loop+1} ---")
        for _ in range(total_slides):
            current_src = slider.get_active_slide_src()
            visited.append(current_src)
            print(f"Slide: {current_src}")
            slider.click_next()

    print("Visited slides:", len(set(visited)))
    time.sleep(2)
