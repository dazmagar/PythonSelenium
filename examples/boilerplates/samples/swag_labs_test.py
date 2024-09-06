"""Classic Page Object Model with BaseCase inheritance."""

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class LoginPage:
    def login_to_swag_labs(self, ps, username):
        ps.open("https://www.saucedemo.com")
        ps.type("#user-name", username)
        ps.type("#password", "secret_sauce")
        ps.click('input[type="submit"]')


class MyTests(BaseCase):
    def test_swag_labs_login(self):
        LoginPage().login_to_swag_labs(self, "standard_user")
        self.assert_element("div.inventory_list")
        self.assert_element('div:contains("Sauce Labs Backpack")')
        self.js_click("a#logout_sidebar_link")
        self.assert_element("div#login_button_container")
