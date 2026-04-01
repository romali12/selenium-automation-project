def test_homepage_title(driver):
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    assert "Example" in driver.title
