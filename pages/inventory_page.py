from selenium.webdriver.common.by import By

class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def get_cart_count(self):
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()