<!-- PythonSelenium Docs -->

## 🐝 Behave test runner for PythonSelenium 🐝

🐝 (Utilizes the [Behave BDD Python library](https://github.com/behave/behave). For more info, see the [Behave tutorial](https://behave.readthedocs.io/en/stable/tutorial.html) and read about [Behave's Gherkin model](https://behave.readthedocs.io/en/stable/gherkin.html).)

🐝 Behave examples with PythonSelenium: [PythonSelenium/examples/behave_bdd](/examples/behave_bdd)

```bash
> cd examples/behave_bdd/
> behave features/swag_labs.feature -T -D dashboard -k

Dashboard: /examples/behave_bdd/dashboard.html
********************************************************************************
Feature: PythonSelenium scenarios for the Swag Labs App # features/swag_labs.feature:1

  Background:   # features/swag_labs.feature:3

  Scenario: User can log in and log out successfully  # features/swag_labs.feature:6
    Given Open the Swag Labs Login Page               # features/steps/swag_labs.py:4
    When Login to Swag Labs with standard_user        # features/steps/swag_labs.py:11
    Then Verify that the current user is logged in    # features/steps/swag_labs.py:18
    When Logout from Swag Labs                        # features/steps/swag_labs.py:136
    Then Verify on Login page                         # features/steps/swag_labs.py:142
   ✅ Scenario Passed!

- Dashboard: /examples/behave_bdd/dashboard.html
--- LogPath: /examples/behave_bdd/latest_logs/
==================================================================================
1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 8 skipped
5 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m1.101s
```

### 🐝 Behave-Gherkin files:

🐝 The ``*.feature`` files can use any step seen from:

```bash
behave --steps-catalog
```

🐝 PythonSelenium includes several pre-made Behave steps, which you can use by creating a Python file with the following line in your ``features/steps/`` directory:

```python
from pythonselenium.behave import steps  # noqa
```

🐝 Inside your ``features/environment.py`` file, you should have the following:

```python
from pythonselenium import BaseCase
from pythonselenium.behave import behave_ps
behave_ps.set_base_class(BaseCase)  # Accepts a BaseCase subclass
from pythonselenium.behave.behave_ps import before_all  # noqa
from pythonselenium.behave.behave_ps import before_feature  # noqa
from pythonselenium.behave.behave_ps import before_scenario  # noqa
from pythonselenium.behave.behave_ps import before_step  # noqa
from pythonselenium.behave.behave_ps import after_step  # noqa
from pythonselenium.behave.behave_ps import after_scenario  # noqa
from pythonselenium.behave.behave_ps import after_feature  # noqa
from pythonselenium.behave.behave_ps import after_all  # noqa
```

🐝 If you've already created a subclass of ``BaseCase`` with custom methods, you can swap ``BaseCase`` in with your own subclass, which will allow you to easily use your own custom methods in your Behave step definitions.

🐝 Here's an example Python file in the ``features/steps/`` folder:

```python
from behave import step


@step("Open the Swag Labs Login Page")
def go_to_swag_labs(context):
    ps = context.ps
    ps.open("https://www.saucedemo.com")
    ps.clear_local_storage()


@step("Login to Swag Labs with {user}")
def login_to_swag_labs(context, user):
    ps = context.ps
    ps.type("#user-name", user)
    ps.type("#password", "secret_sauce\n")


@step("Verify that the current user is logged in")
def verify_logged_in(context):
    ps = context.ps
    ps.assert_element("#header_container")
    ps.assert_element("#react-burger-menu-btn")
    ps.assert_element("#shopping_cart_container")


@step('Add "{item}" to cart')
def add_item_to_cart(context, item):
    context.ps.click('div.inventory_item:contains("%s") button[name*="add"]' % item)
```

🐝 A ``*.feature`` file could look like this:

```gherkin
Feature: PythonSelenium scenarios for the Swag Labs App

  Background:
    Given Open the Swag Labs Login Page

  Scenario: User can order a backpack from the store
    When Login to Swag Labs with standard_user
    Then Verify that the current user is logged in
    And Save price of "Backpack" to <item_price>
    When Add "Backpack" to cart
    Then Verify shopping cart badge shows 1 item(s)
    When Click on shopping cart icon
    And Click Checkout
    And Enter checkout info: First, Last, 12345
    And Click Continue
    Then Verify 1 "Backpack" in cart
    And Verify cost of "Backpack" is <item_price>
    And Verify item total is $29.99
    And Verify tax amount is $2.40
    And Verify total cost is $32.39
    When Click Finish
    Then Verify order complete
    When Logout from Swag Labs
    Then Verify on Login page
```

🐝🎖️ For convenience, the [PythonSelenium Behave GUI](/examples/behave_bdd) lets you run ``behave`` scripts from a Desktop app.
🐝🎖️ To launch it, call ``pysel behave-gui`` or ``pysel gui-behave``:

```bash
pysel behave-gui
* Starting the PythonSelenium Behave Commander GUI App...
```
🐝🎖️ You can customize the tests that show up there:

```bash
pysel behave-gui  # all tests
pysel behave-gui -i=swag  # tests with "swag" in the name
pysel behave-gui features/  # tests located in the "features/" folder
pysel behave-gui features/swag_labs.feature  # tests in that feature
```

--------
