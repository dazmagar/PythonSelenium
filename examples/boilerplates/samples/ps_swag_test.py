"""Classic Page Object Model with the "ps" fixture."""

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class LoginPage:
    def login_to_swag_labs(self, ps, username):
        ps.open("https://www.saucedemo.com")
        ps.type("#user-name", username)
        ps.type("#password", "secret_sauce")
        ps.click('input[type="submit"]')


class MyTests:
    def test_swag_labs_login(self, ps):
        LoginPage().login_to_swag_labs(ps, "standard_user")
        ps.assert_element("div.inventory_list")
        ps.assert_element('div:contains("Sauce Labs Backpack")')
        ps.js_click("a#logout_sidebar_link")
        ps.assert_element("div#login_button_container")
