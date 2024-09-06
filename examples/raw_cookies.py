"""A PythonSelenium test that loads cookies to bypass login."""

from pythonselenium import PS

# Log in to Swag Labs and save cookies
with PS(test=True) as ps:
    ps.open("https://www.saucedemo.com")
    ps.wait_for_element("div.login_logo")
    ps.type("#user-name", "standard_user")
    ps.type("#password", "secret_sauce")
    ps.click('input[type="submit"]')
    ps.highlight("div.inventory_list", loops=6)
    ps.save_cookies(name="cookies.txt")

# Load previously saved cookies to bypass login
with PS(test=True) as ps:
    ps.open("https://www.saucedemo.com")
    ps.load_cookies(name="cookies.txt")
    ps.open("https://www.saucedemo.com/inventory.html")
    ps.highlight("div.inventory_list", loops=12)
