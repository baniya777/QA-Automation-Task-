# Handles everything on the inventory/products page
from selenium.webdriver.common.by import By

class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        # Add products to cart - using its specific button ID, I chose backpack
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def get_cart_count(self):
        # Return the number shown on the cart icon
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

    def go_to_cart(self):
        # Click the cart icon to go to cart page
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def checkout(self):
         # Click the Checkout button on the cart page
        self.driver.find_element(By.ID, "checkout").click()