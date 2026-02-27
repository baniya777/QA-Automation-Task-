# Login page actions - everything related to logging is here
from selenium.webdriver.common.by import By
class LoginPage:

    def __init__(self, driver):
        # Initialize with the browser driver
        self.driver = driver

    def open(self):
        # Go to the demo site
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        # Fill in the form and hit login
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def get_error(self):
        # Return the error message when login fails
        return self.driver.find_element(By.CSS_SELECTOR, "h3").text