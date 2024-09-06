from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


# "ps" pytest fixture test in a method with no class
def test_ps_fixture_with_no_class(ps):
    ps.open("https://www.saucedemo.com")
    ps.wait_for_element("div.login_logo")
    ps.type("#user-name", "standard_user")
    ps.type("#password", "secret_sauce")
    ps.click('input[type="submit"]')
    ps.highlight("div.inventory_list", loops=6)


# "ps" pytest fixture test in a method inside a class
class Test_ps_Fixture:
    def test_ps_fixture_inside_class(self, ps):
        ps.open("https://www.saucedemo.com")
        ps.wait_for_element("div.login_logo")
        ps.type("#user-name", "standard_user")
        ps.type("#password", "secret_sauce")
        ps.click('input[type="submit"]')
        ps.highlight("div.inventory_list", loops=6)
