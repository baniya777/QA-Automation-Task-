# Cart and checkout tests
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_cart(driver):
    # checking if a product can be added to cart successfully
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_to_cart()

    assert inventory.get_cart_count() == "1"

def test_checkout(driver):
    # verifying full checkour flow: add to cart ---> go to checkout --> proceed checkout
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_to_cart()
    inventory.go_to_cart()
    inventory.checkout()

    assert "checkout-step-one" in driver.current_url