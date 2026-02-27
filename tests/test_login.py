from pages.login_page import LoginPage

def test_valid_login(driver):

    login = LoginPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url


def test_invalid_login(driver):

    login = LoginPage(driver)

    login.open()
    login.login("wrong", "wrong")

    assert "Epic sadface" in login.get_error()