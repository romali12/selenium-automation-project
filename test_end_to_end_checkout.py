#pytest -m smoke //Tagging
#pytest -n 10 //pytest-xdist plugin you need to run in parallel

import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage
from pages.confirmation_page import ConfirmationPage

def test_end_to_end_checkout(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    overview = OverviewPage(driver)
    confirmation = ConfirmationPage(driver)

    #Login
    login.load()
    login.login("standard_user", "secret_sauce")
    time.sleep(3)

    #Add product to cart
    inventory.add_first_product_to_cart()
    inventory.go_to_cart()
    time.sleep(3)

    #Checkout
    cart.click_checkout()
    checkout.fill_checkout_info("Rohan", "Sharma", "411001")
    time.sleep(3)

    #Confirm order
    overview.click_finish()
    time.sleep(3)

    #Validate order success
    msg = confirmation.get_confirmation_message()
    assert msg == "Thank you for your order!", f"Unexpected message: {msg}"
    time.sleep(3)
