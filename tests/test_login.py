# Login tests - valid and invalid scenarios
from pages.login_page import LoginPage

def test_valid_login(driver):
    # verifying that valid credentials then gors to inventory page
    login = LoginPage(driver)
    
    login.open()
    login.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url


def test_invalid_login(driver):
    # verifying that invalid credentials shows an error msg
    login = LoginPage(driver)

    login.open()
    login.login("wrong", "wrong")

    assert "Username and password do not match" in login.get_error()
