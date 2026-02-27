from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_cart(driver):

    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_to_cart()

    assert inventory.get_cart_count() == "1"


def test_checkout(driver):

    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_to_cart()
    inventory.go_to_cart()
    inventory.checkout()

    assert "checkout-step-one" in driver.current_url