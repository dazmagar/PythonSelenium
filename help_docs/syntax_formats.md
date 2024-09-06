<!-- PythonSelenium Docs -->

<a id="syntax_formats"></a>

<h2>The 14 Syntax Formats / Design Patterns</h2>

<h3>🔡 PythonSelenium supports multiple ways of structuring tests:</h3>

<blockquote>
<p dir="auto"></p>
<ul dir="auto">
<li><a href="#ps_sf_01"><strong>01. BaseCase direct class inheritance</strong></a></li>
<li><a href="#ps_sf_02"><strong>02. BaseCase subclass inheritance</strong></a></li>
<li><a href="#ps_sf_03"><strong>03. The "ps" pytest fixture (no class)</strong></a></li>
<li><a href="#ps_sf_04"><strong>04. The "ps" pytest fixture (in class)</strong></a></li>
<li><a href="#ps_sf_05"><strong>05. Page Object Model with BaseCase</strong></a></li>
<li><a href="#ps_sf_06"><strong>06. Page Object Model with the "ps" fixture</strong></a></li>
<li><a href="#ps_sf_07"><strong>07. Using "request" to get "ps" (no class)</strong></a></li>
<li><a href="#ps_sf_08"><strong>08. Using "request" to get "ps" (in class)</strong></a></li>
<li><a href="#ps_sf_09"><strong>09. Overriding the driver via BaseCase</strong></a></li>
<li><a href="#ps_sf_10"><strong>10. Overriding the driver via "ps" fixture</strong></a></li>
<li><a href="#ps_sf_11"><strong>11. Gherkin syntax with "behave" BDD runner</strong></a></li>
<li><a href="#ps_sf_12"><strong>12. PythonSelenium PS (Python context manager)</strong></a></li>
<li><a href="#ps_sf_13"><strong>13. The driver manager (via context manager)</strong></a></li>
<li><a href="#ps_sf_14"><strong>14. The driver manager (via direct import)</strong></a></li>
</ul>
</blockquote>

--------

<a id="ps_sf_01"></a>
<h2>1. BaseCase direct class inheritance</h2>

In this format, (which is used by most of the tests in the [PythonSelenium examples folder](/examples)), <code>BaseCase</code> is imported at the top of a Python file, followed by a Python class inheriting <code>BaseCase</code>. Then, any test method defined in that class automatically gains access to PythonSelenium methods, including the <code>setUp()</code> and <code>tearDown()</code> methods that are automatically called for opening and closing web browsers at the start and end of tests.

To run a test of this format, use **``pytest``** or ``pynose``. Adding ``BaseCase.main(__name__, __file__)`` enables ``python`` to run ``pytest`` on your file indirectly. Here's an example:

```python
from pythonselenium import BaseCase
BaseCase.main(__name__, __file__)

class MyTestClass(BaseCase):
    def test_demo_site(self):
        self.load_html_file("examples/offline_examples/demo_page.html")
        self.type("#myTextInput", "This is Automated")
        self.click("#myButton")
        self.assert_element("tbody#tbodyId")
        self.assert_text("Automation Practice", "h3")
        self.click_link("PythonSelenium Demo Page")
        self.assert_exact_text("Demo Page", "h1")
        self.assert_no_js_errors()
```

(See [examples/test_demo_site.py](/examples/test_demo_site.py) for the full test.)

Using ``BaseCase`` inheritance is a great starting point for anyone learning PythonSelenium, and it follows good object-oriented programming principles.

<a id="ps_sf_02"></a>
<h2>2. BaseCase subclass inheritance</h2>

There are situations where you may want to customize the <code>setUp</code> and <code>tearDown</code> of your tests. Maybe you want to have all your tests login to a specific web site first, or maybe you want to have your tests report results through an API call depending on whether a test passed or failed. <b>This can be done by creating a subclass of <code>BaseCase</code> and then carefully creating custom <code>setUp()</code> and <code>tearDown()</code> methods that don't overwrite the critical functionality of the default PythonSelenium <code>setUp()</code> and <code>tearDown()</code> methods.</b> Afterwards, your test classes will inherit the subclass of <code>BaseCase</code> with the added functionality, rather than directly inheriting <code>BaseCase</code> itself. Here's an example of that:

```python
from pythonselenium import BaseCase
BaseCase.main(__name__, __file__)

class BaseTestCase(BaseCase):
    def setUp(self):
        super().setUp()
        # <<< Run custom setUp() code for tests AFTER the super().setUp() >>>

    def tearDown(self):
        self.save_teardown_screenshot()  # On failure or "--screenshot"
        if self.has_exception():
            # <<< Run custom code if the test failed. >>>
            pass
        else:
            # <<< Run custom code if the test passed. >>>
            pass
        # (Wrap unreliable tearDown() code in a try/except block.)
        # <<< Run custom tearDown() code BEFORE the super().tearDown() >>>
        super().tearDown()

    def login(self):
        # <<< Placeholder. Add your code here. >>>
        # Reduce duplicate code in tests by having reusable methods like this.
        # If the UI changes, the fix can be applied in one place.
        pass

    def example_method(self):
        # <<< Placeholder. Add your code here. >>>
        pass

class MyTests(BaseTestCase):
    def test_example(self):
        self.login()
        self.example_method()
        self.type("input", "Name")
        self.click("form button")
        # ...
```

(See [examples/boilerplates/base_test_case.py](/examples/boilerplates/base_test_case.py) for more info.)

<a id="ps_sf_03"></a>
<h2>3. The "ps" pytest fixture (no class)</h2>

The pytest framework comes with a unique system called fixtures, which replaces import statements at the top of Python files by importing libraries directly into test definitions. More than just being an import, a pytest fixture can also automatically call predefined <code>setUp()</code> and <code>tearDown()</code> methods at the beginning and end of test methods. To work, <code>ps</code> is added as an argument to each test method definition that needs PythonSelenium functionality. This means you no longer need import statements in your Python files to use PythonSelenium. <b>If using other pytest fixtures in your tests, you may need to use the PythonSelenium fixture (instead of <code>BaseCase</code> class inheritance) for compatibility reasons.</b> Here's an example of the <code>ps</code> fixture in a test that does not use Python classes:

```python
def test_ps_fixture_with_no_class(ps, username):
    ps.open("https://www.saucedemo.com")
    ps.type("#user-name", username)
    ps.type("#password", "secret_sauce")
    ps.click('input[type="submit"]')
```

<a id="ps_sf_04"></a>
<h2>4. The "ps" pytest fixture (in class)</h2>

The <code>ps</code> pytest fixture can also be used inside of a class. There is a slight change to the syntax because that means test methods must also include <code>self</code> in their argument definitions when test methods are defined. (The <code>self</code> argument represents the class object, and is used in every test method that lives inside of a class.) Once again, no import statements are needed in your Python files for this to work. Here's an example of using the <code>ps</code> fixture in a test method that lives inside of a Python class:

```python
class Test_PS_Fixture:
    def test_ps_fixture_inside_class(self, ps, username):
        ps.open("https://www.saucedemo.com")
        ps.type("#user-name", username)
        ps.type("#password", "secret_sauce")
        ps.click('input[type="submit"]')
```

<a id="ps_sf_05"></a>
<h2>5. Page Object Model with BaseCase</h2>

With PythonSelenium, you can use Page Objects to break out code from tests, but remember, the <code>self</code> variable (from test methods that inherit <code>BaseCase</code>) contains the driver and all other framework-specific variable definitions. Therefore, that <code>self</code> must be passed as an arg into any outside class method in order to call PythonSelenium methods from there. In the example below, the <code>self</code> variable from the test method is passed into the <code>ps</code> arg of the Page Object class method because the <code>self</code> arg of the Page Object class method is already being used for its own class. Every Python class method definition must include the <code>self</code> as the first arg.

```python
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
```

(See [examples/boilerplates/samples/swag_labs_test.py](/examples/boilerplates/samples/swag_labs_test.py) for the full test.)

<a id="ps_sf_06"></a>
<h2>6. Page Object Model with the "ps" fixture</h2>

This is similar to the classic Page Object Model with <code>BaseCase</code> inheritance, except that this time we pass the <code>ps</code> pytest fixture from the test into the <code>ps</code> arg of the page object class method, (instead of passing <code>self</code>). Now that you're using <code>ps</code> as a pytest fixture, you no longer need to import <code>BaseCase</code> anywhere in your code. See the example below:

```python
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
```

(See [examples/boilerplates/samples/ps_swag_test.py](/examples/boilerplates/samples/ps_swag_test.py) for the full test.)

<a id="ps_sf_07"></a>
<h2>7. Using "request" to get "ps" (no class)</h2>

The pytest <code>request</code> fixture can be used to retrieve other pytest fixtures from within tests, such as the <code>ps</code> fixture. This allows you to have more control over when fixtures get initialized because the fixture no longer needs to be loaded at the very beginning of test methods. This is done by calling <code>request.getfixturevalue('ps')</code> from the test. Here's an example of using the pytest <code>request</code> fixture to load the <code>ps</code> fixture in a test method that does not use Python classes:

```python
def test_request_ps_fixture(request):
    ps = request.getfixturevalue("ps")
    ps.load_html_file("examples/offline_examples/demo_page.html")
    ps.assert_text("PythonSelenium", "#myForm h2")
    ps.assert_element("input#myTextInput")
    ps.type("#myTextarea", "This is me")
    ps.click("#myButton")
    ps.tearDown()
```

(See the top of [examples/test_request_ps_fixture.py](/examples/test_request_ps_fixture.py) for the test.)

<a id="ps_sf_08"></a>
<h2>8. Using "request" to get "ps" (in class)</h2>

The pytest <code>request</code> fixture can also be used to get the <code>ps</code> fixture from inside a Python class. Here's an example of that:

```python
class Test_Request_Fixture:
    def test_request_ps_fixture_in_class(self, request):
        ps = request.getfixturevalue('ps')
        ps.load_html_file("examples/offline_examples/demo_page.html")
        ps.assert_element("input#myTextInput")
        ps.type("#myTextarea", "Automated")
        ps.assert_text("This Text is Green", "#pText")
        ps.click("#myButton")
        ps.assert_text("This Text is Purple", "#pText")
        ps.tearDown()
```

(See the bottom of [examples/test_request_ps_fixture.py](/examples/test_request_ps_fixture.py) for the test.)

<a id="ps_sf_09"></a>
<h2>9. Overriding the driver via BaseCase</h2>

When you want to use PythonSelenium methods via <code>BaseCase</code>, but you want total freedom to control how you spin up your web browsers, this is the format you want. Although PythonSelenium gives you plenty of command-line options to change how your browsers are launched, this format gives you more control when the existing options aren't enough. Here's an example of that:

```python
from selenium import webdriver
from pythonselenium import BaseCase
BaseCase.main(__name__, __file__)

class OverrideDriverTest(BaseCase):
    def get_new_driver(self, *args, **kwargs):
        """This method overrides get_new_driver() from BaseCase."""
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-3d-apis")
        options.add_argument("--disable-notifications")
        if self.headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation", "enable-logging"],
        )
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        }
        options.add_experimental_option("prefs", prefs)
        return webdriver.Chrome(options=options)

    def test_simple(self):
        self.load_html_file("examples/offline_examples/demo_page.html")
        self.assert_text("Demo Page", "h1")
```

(From [examples/test_override_driver.py](/examples/test_override_driver.py))

The above format lets you customize [selenium-wire](https://github.com/wkeeling/selenium-wire) for intercepting and inspecting requests and responses during PythonSelenium tests. Here's how a ``selenium-wire`` integration may look:

```python
from pythonselenium import BaseCase
from seleniumwire import webdriver  # Requires "pip install selenium-wire"
BaseCase.main(__name__, __file__)


class WireTestCase(BaseCase):
    def get_new_driver(self, *args, **kwargs):
        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"]
        )
        options.add_experimental_option("useAutomationExtension", False)
        return webdriver.Chrome(options=options)

    def test_simple(self):
        self.load_html_file("examples/offline_examples/demo_page.html")
        for request in self.driver.requests:
            print(request.url)
```

(NOTE: The ``selenium-wire`` integration is now included with ``pythonselenium``: Add ``--wire`` as a ``pytest`` command-line option to activate.)

<a id="ps_sf_10"></a>
<h2>10. Overriding the driver via "ps" fixture</h2>

When you want to use PythonSelenium methods via the ``ps`` pytest fixture, but you want total freedom to control how you spin up your web browsers, this is the format you want. Although PythonSelenium gives you plenty of command-line options to change how your browsers are launched, this format gives you more control when the existing options aren't enough.

```python
"""Overriding the "ps" fixture to override the driver."""
import pytest

@pytest.fixture()
def ps(request):
    from selenium import webdriver
    from pythonselenium import BaseCase
    from pythonselenium import config as ps_config
    from pythonselenium.core import session_helper

    class BaseClass(BaseCase):
        def get_new_driver(self, *args, **kwargs):
            """This method overrides get_new_driver() from BaseCase."""
            options = webdriver.ChromeOptions()
            if self.headless:
                options.add_argument("--headless=new")
                options.add_argument("--disable-gpu")
            options.add_experimental_option(
                "excludeSwitches", ["enable-automation"],
            )
            return webdriver.Chrome(options=options)

        def setUp(self):
            super().setUp()

        def base_method(self):
            pass

        def tearDown(self):
            self.save_teardown_screenshot()  # On failure or "--screenshot"
            super().tearDown()

    if request.cls:
        if ps_config.reuse_class_session:
            the_class = str(request.cls).split(".")[-1].split("'")[0]
            if the_class != ps_config._ps_class:
                session_helper.end_reused_class_session_as_needed()
                ps_config._ps_class = the_class
        request.cls.ps = BaseClass("base_method")
        request.cls.ps.setUp()
        request.cls.ps._needs_tearDown = True
        request.cls.ps._using_ps_fixture = True
        request.cls.ps._using_ps_fixture_class = True
        ps_config._ps_node[request.node.nodeid] = request.cls.ps
        yield request.cls.ps
        if request.cls.ps._needs_tearDown:
            request.cls.ps.tearDown()
            request.cls.ps._needs_tearDown = False
    else:
        ps = BaseClass("base_method")
        ps.setUp()
        ps._needs_tearDown = True
        ps._using_ps_fixture = True
        ps._using_ps_fixture_no_class = True
        ps_config._ps_node[request.node.nodeid] = ps
        yield ps
        if ps._needs_tearDown:
            ps.tearDown()
            ps._needs_tearDown = False

def test_override_fixture_no_class(ps):
    ps.load_html_file("examples/offline_examples/demo_page.html")
    ps.type("#myTextInput", "This is Automated")

class TestOverride:
    def test_override_fixture_inside_class(self, ps):
        ps.load_html_file("examples/offline_examples/demo_page.html")
        ps.type("#myTextInput", "This is Automated")
```

(From [examples/test_override_ps_fixture.py](/examples/test_override_ps_fixture.py))

Here's how the [selenium-wire](https://github.com/wkeeling/selenium-wire) integration may look when overriding the ``ps`` pytest fixture to override the driver:

```python
import pytest

@pytest.fixture()
def ps(request):
    import sys
    from pythonselenium import BaseCase
    from pythonselenium import config as ps_config
    from seleniumwire import webdriver  # Requires "pip install selenium-wire"

    class BaseClass(BaseCase):
        def get_new_driver(self, *args, **kwargs):
            options = webdriver.ChromeOptions()
            if "linux" in sys.platform:
                options.add_argument("--headless=new")
            options.add_experimental_option(
                "excludeSwitches", ["enable-automation"],
            )
            return webdriver.Chrome(options=options)

        def setUp(self):
            super().setUp()

        def tearDown(self):
            self.save_teardown_screenshot()  # On failure or "--screenshot"
            super().tearDown()

        def base_method(self):
            pass

    if request.cls:
        request.cls.ps = BaseClass("base_method")
        request.cls.ps.setUp()
        request.cls.ps._needs_tearDown = True
        request.cls.ps._using_ps_fixture = True
        request.cls.ps._using_ps_fixture_class = True
        ps_config._ps_node[request.node.nodeid] = request.cls.ps
        yield request.cls.ps
        if request.cls.ps._needs_tearDown:
            request.cls.ps.tearDown()
            request.cls.ps._needs_tearDown = False
    else:
        ps = BaseClass("base_method")
        ps.setUp()
        ps._needs_tearDown = True
        ps._using_ps_fixture = True
        ps._using_ps_fixture_no_class = True
        ps_config._ps_node[request.node.nodeid] = ps
        yield ps
        if ps._needs_tearDown:
            ps.tearDown()
            ps._needs_tearDown = False

def test_wire_with_no_class(ps):
    ps.load_html_file("examples/offline_examples/demo_page.html")
    for request in ps.driver.requests:
        print(request.url)

class TestWire:
    def test_wire_inside_class(self, ps):
        ps.load_html_file("examples/offline_examples/demo_page.html")
        for request in ps.driver.requests:
            print(request.url)
```

(NOTE: The ``selenium-wire`` integration is now included with ``pythonselenium``: Add ``--wire`` as a ``pytest`` command-line option to activate. If you need both ``--wire`` with ``--undetected`` modes together, you'll still need to override ``get_new_driver()``.)

<a id="ps_sf_11"></a>
<h2>11. Gherkin syntax with "behave" BDD runner</h2>

With [Behave's BDD Gherkin format](https://behave.readthedocs.io/en/stable/gherkin.html), you can use natural language to write tests that work with PythonSelenium methods. Behave tests are run by calling ``behave`` on the command-line. This requires some special files in a specific directory structure. Here's an example of that structure:

```bash
features/
├── __init__.py
├── behave.ini
├── environment.py
├── feature_file.feature
└── steps/
    ├── __init__.py
    ├── imported.py
    └── step_file.py
```

A ``*.feature`` file might look like this:

```gherkin
Feature: PythonSelenium scenarios for the Swag Labs App

  Background:
    Given Open the Swag Labs Login Page

  Scenario: User can log in and log out successfully
    When Login to Swag Labs with standard_user
    Then Verify that the current user is logged in
    When Logout from Swag Labs
    Then Verify on Login page
```

(From [examples/behave_bdd/features/swag_labs.feature](/examples/behave_bdd/features/swag_labs.feature))

You'll need the ``environment.py`` file for tests to work. Here it is:

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

(From [examples/behave_bdd/features/environment.py](/examples/behave_bdd/features/environment.py))

Inside that file, you can use ``BaseCase`` (or a subclass) for the inherited class.

For your ``behave`` tests to have access to PythonSelenium Behave steps, you can create an ``imported.py`` file with the following line:

```python
from pythonselenium.behave import steps  # noqa
```

That will allow you to use lines like this in your ``*.feature`` files:

```gherkin
Feature: PythonSelenium scenarios for the Swag Labs App

  Background:
    Given Open the Swag Labs Login Page

  Scenario: User can log in and log out successfully
    When Login to Swag Labs with standard_user
    Then Verify that the current user is logged in
    When Logout from Swag Labs
    Then Verify on Login page
```

You can also create your own step files (Eg. ``step_file.py``):

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
```

(For more information, see the [PythonSelenium Behave BDD ReadMe](/examples/behave_bdd/ReadMe.md).)

<a id="ps_sf_12"></a>
<h2>12. PythonSelenium PS (Python context manager)</h2>

This format provides a pure Python way of using PythonSelenium without a test runner. Options can be passed via method instantiation or from the command-line. When setting the <code>test</code> option to <code>True</code> (or calling <code>python --test</code>), then standard test logging will occur, such as screenshots and reports for failing tests. All the usual PythonSelenium options are available, such as customizing the browser settings, etc. Here are some examples:

```python
from pythonselenium import PS

with PS(uc=True, test=True) as ps:
    url = "https://www.bing.com/turing/captcha/challenge"
    ps.uc_open_with_reconnect(url, 4)
    ps.uc_gui_click_captcha()
```

(See [examples/raw_bing_captcha.py](/examples/raw_bing_captcha.py) for the test.)

Here's another example, which uses <code>test</code> mode:

```python
from pythonselenium import PS

with PS(test=True) as ps:
    ps.open("https://google.com/ncr")
    ps.type('[name="q"]', "Selenium on GitHub\n")
    ps.click('a[href*="github.com/SeleniumHQ/selenium"]')
    ps.highlight("div.Layout-main")
    ps.highlight("div.Layout-sidebar")
    ps.sleep(0.5)

with PS(test=True, rtf=True, demo=True) as ps:
    ps.load_html_file("examples/offline_examples/demo_page.html")
    ps.type("#myTextInput", "This is Automated")
    ps.assert_text("This is Automated", "#myTextInput")
    ps.assert_text("This Text is Green", "#pText")
    ps.click('button:contains("Click Me")')
    ps.assert_text("This Text is Purple", "#pText")
    ps.click("#checkBox1")
    ps.assert_element_not_visible("div#drop2 img#logo")
    ps.drag_and_drop("img#logo", "div#drop2")
    ps.assert_element("div#drop2 img#logo")
```

<a id="ps_sf_13"></a>
<h2>13. The driver manager (via context manager)</h2>

This pure Python format gives you a raw <code>webdriver</code> instance in a <code>with</code> block. The PythonSelenium Driver Manager will automatically make sure that your driver is compatible with your browser version. It gives you full access to customize driver options via method args or via the command-line. The driver will automatically call <code>quit()</code> after the code leaves the <code>with</code> block. Here are some examples:

```python
"""DriverContext() example. (Runs with "python")."""
from pythonselenium import DriverContext

with DriverContext(browser="chrome", incognito=True) as driver:
    driver.open("https://google.com/ncr")
    driver.highlight('[name="q"]', loops=6)
```

(See [examples/raw_driver_context.py](/examples/raw_driver_context.py) for an example.)

<a id="ps_sf_14"></a>
<h2>14. The driver manager (via direct import)</h2>

Another way of running Selenium tests with pure ``python`` (as opposed to using ``pytest`` or ``pynose``) is by using this format, which bypasses [BaseCase](/pythonselenium/fixtures/base_case.py) methods while still giving you a flexible driver with a manager. PythonSelenium includes helper files such as [page_actions.py](/pythonselenium/fixtures/page_actions.py), which may help you get around some of the limitations of bypassing ``BaseCase``. Here's an example:

```python
"""Driver() example. (Runs with "python")."""
from pythonselenium import Driver

driver = Driver(browser="chrome", headless=False)
try:
    driver.load_html_file("examples/offline_examples/demo_page.html")
    driver.highlight("h2")
    driver.type("#myTextInput", "Automation")
    driver.click("#checkBox1")
    driver.highlight("img", loops=6)
finally:
    driver.quit()
```

(From [examples/raw_driver_manager.py](/examples/raw_driver_manager.py))

Here's how the [selenium-wire](https://github.com/wkeeling/selenium-wire) integration may look when using the ``Driver()`` format:

```python
from pythonselenium import Driver

driver = Driver(wire=True, headless=True)
try:
    driver.get("https://wikipedia.org")
    for request in driver.requests:
        print(request.url)
finally:
    driver.quit()
```

Here's another `selenium-wire` example with the `Driver()` format:

```python
from pythonselenium import Driver

def intercept_response(request, response):
    print(request.headers)

driver = Driver(wire=True)
try:
    driver.response_interceptor = intercept_response
    driver.get("https://wikipedia.org")
finally:
    driver.quit()
```

The ``Driver()`` manager format can be used as a drop-in replacement for virtually every Python/selenium framework, as it uses the raw ``driver`` instance for handling commands. The ``Driver()`` method simplifies the work of managing drivers with optimal settings, and it can be configured with multiple args. The ``Driver()`` also accepts command-line options (such as ``python --headless``) so that you don't need to modify your tests directly to use different settings. These command-line options only take effect if the associated method args remain unset (or set to ``None``) for the specified options.

When using the ``Driver()`` format, you may need to activate a Virtual Display on your own if you want to run headed tests in a headless Linux environment. (See https://github.com/mdmintz/psVirtualDisplay for details.) One such example of this is using an authenticated proxy, which is configured via a Chrome extension that is generated at runtime. (Note that regular headless mode in Chrome doesn't support extensions.)

--------

