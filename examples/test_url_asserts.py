from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class URLTestClass(BaseCase):
    def test_url_asserts(self):
        self.open("https://coffee-cart.app/")
        self.assert_url("https://coffee-cart.app/")
        self.assert_title_contains("Coffee cart")
        self.assert_title("Coffee cart")
