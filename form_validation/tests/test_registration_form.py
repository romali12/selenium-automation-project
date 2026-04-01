from pages.registration_page import RegistrationPage

def test_registration_form_submission(driver):
    page = RegistrationPage(driver)
    page.load()
    page.fill_form("Test", "User", "testUser@gmail.com", "9854002134")
    page.submit()
    assert "WebTable" not in driver.current_url, "Form may not have submitted correctly."
