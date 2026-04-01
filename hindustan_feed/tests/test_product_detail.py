import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://hf.redliodesigns.com/products/kanak-senior"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_image_scroll(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    first_image = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//button[@aria-label='Go to Slide 2' and contains(@class, 'image-gallery-thumbnail')]"
    )))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_image)
    first_image.click()
    time.sleep(3)

    second_image = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//button[@aria-label='Go to Slide 3' and contains(@class, 'image-gallery-thumbnail')]"
    )))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", second_image)
    second_image.click()
    time.sleep(3)

    third_image = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//button[@aria-label='Go to Slide 4' and contains(@class, 'image-gallery-thumbnail')]"
    )))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", third_image)
    third_image.click()
    time.sleep(3)

def test_wishlist_icon(driver):
    driver.get(BASE_URL)
    driver.find_element(By.XPATH,"//img[@alt='Wishlist']").click()
    time.sleep(2)

def test_button_function(driver):
    driver.get(BASE_URL)
    pdf_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space(text())='Download brochure/leaflet']"))
    )
    pdf_link = pdf_button.get_attribute("href")
    assert pdf_link == "https://hindustanfeeds.com/wp-content/uploads/2021/02/Hf-Sphurti.pdf", \
        f"Unexpected PDF link: {pdf_link}"
    pdf_button.click()
    time.sleep(2)

def test_inquiry_btn(driver):
    driver.get(BASE_URL)
    inquiry_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Make an Inquiry']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", inquiry_btn)
    inquiry_btn.click()
    popup_modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'modal-content')]"))
    )
    assert popup_modal.is_displayed(), "Popup did not appear after clicking Make an Inquiry"
    time.sleep(3)

def test_dosage_button(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    dosage_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Dosage Calculator']"))
    )
    time.sleep(1)

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", dosage_btn)
    dosage_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Dosage Calculator']"))
    )
    time.sleep(1)

    dosage_btn.click()
    time.sleep(3)

def test_faq_tabs(driver):
    driver.get(BASE_URL)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 1.5);")
    time.sleep(2)
    wait = WebDriverWait(driver, 10)
    for question in ["Question - 2", "Question - 3", "Question - 4"]:
        faq_btn = wait.until(EC.presence_of_element_located((
            By.XPATH,
            f"//button[@type='button' and normalize-space()='{question}']"
        )))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", faq_btn)
        time.sleep(1)

        driver.execute_script("arguments[0].click();", faq_btn)
        time.sleep(2)

def test_similar_product(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 15)

    view_all_btn = wait.until(EC.presence_of_element_located((
        By.XPATH, "//div[@class='ProductDetailPage_viewAll__ny68a']//a"
    )))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", view_all_btn)
    time.sleep(2)

    clickable_btn = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//div[@class='ProductDetailPage_viewAll__ny68a']//a"
    )))
    driver.execute_script("arguments[0].click();", clickable_btn)
    wait.until(EC.url_to_be("https://hf.redliodesigns.com/products?filter=goat"))
    assert driver.current_url == "https://hf.redliodesigns.com/products?filter=goat"
    time.sleep(3)
