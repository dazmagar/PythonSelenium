<!-- PythonSelenium Docs -->

## How PythonSelenium Works 👁️

<a id="how_pythonselenium_works"></a>

👁️🔎 The primary [PythonSelenium syntax format](/help_docs/syntax_formats.md) works by extending [pytest](https://docs.pytest.org/en/latest/) as a direct plugin. PythonSelenium automatically spins up web browsers for tests (using [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/)), and then gives those tests access to the PythonSelenium libraries through the [BaseCase class](/pythonselenium/fixtures/base_case.py). Tests are also given access to [PythonSelenium command-line options](/help_docs/customizing_test_runs.md) and [PythonSelenium methods](/help_docs/method_summary.md), which provide additional functionality.

👁️🔎 ``pytest`` uses a feature called test discovery to automatically find and run Python methods that start with ``test_`` when those methods are located in Python files that start with ``test_`` or end with ``_test.py``.

👁️🔎 The primary [PythonSelenium syntax format](/help_docs/syntax_formats.md) starts by importing ``BaseCase``:

```python
from pythonselenium import BaseCase
```

👁️🔎 This next line activates ``pytest`` when a file is called directly with ``python`` by accident:

```python
BaseCase.main(__name__, __file__)
```

👁️🔎 Classes can inherit ``BaseCase`` to gain PythonSelenium functionality:

```python
class MyTestClass(BaseCase):
```

👁️🔎 Test methods inside ``BaseCase`` classes become PythonSelenium tests: (These tests automatically launch a web browser before starting, and quit the web browser after ending. Default settings can be changed via command-line options.)

```python
class MyTestClass(BaseCase):
    def test_abc(self):
        # ...
```

👁️🔎 [PythonSelenium APIs](/help_docs/method_summary.md) can be called from tests via ``self``:

```python
class MyTestClass(BaseCase):
    def test_abc(self):
        self.open("https://example.com")
```

👁️🔎 Here's what a full test might look like:

```python
from pythonselenium import BaseCase
BaseCase.main(__name__, __file__)

class MyTestClass(BaseCase):
    def test_basics(self):
        self.open("https://www.saucedemo.com")
        self.type("#user-name", "standard_user")
        self.type("#password", "secret_sauce\n")
        self.assert_element("div.inventory_list")
        self.assert_exact_text("Products", "span.title")
        self.click('button[name*="backpack"]')
        self.click("#shopping_cart_container a")
        self.assert_exact_text("Your Cart", "span.title")
        self.assert_text("Backpack", "div.cart_item")
        self.click('button:contains("Remove")')  # HTML innerText
        self.assert_text_not_visible("Backpack", "div.cart_item")
        self.js_click("a#logout_sidebar_link")
        self.assert_element("div#login_button_container")
```

(See the example, [basic_test.py](/examples/basic_test.py), for reference.)

👁️🔎 Here are some examples of running tests with ``pytest``:

```bash
pytest test_mfa_login.py
pytest --headless -n8 --dashboard --html=report.html -v --rs --crumbs
pytest -m marker2
pytest -k agent
pytest offline_examples/
```

👁️🔎 Here's a [PythonSelenium syntax format](/help_docs/syntax_formats.md) that uses the raw `driver`. Unlike the format mentioned earlier, it can be run with `python` instead of `pytest`. The `driver` includes original `driver` methods and new ones added by PythonSelenium:

```python
from pythonselenium import Driver

driver = Driver(browser="chrome", headless=False)
try:
    driver.open("https://github.com/search")
    driver.highlight(".octicon-logo-github:first-of-type", loops=6)
    driver.type("input[aria-label*='Search']", "selenium")
    driver.highlight("input[aria-label*='Search']", loops=6)
finally:
    driver.quit()
```

(See the example, [raw_driver_manager.py](/examples/raw_driver_manager.py), for reference.)

👁️🔎 Note that regular PythonSelenium formats (ones that use `BaseCase`, the `PS` context manager, or the `ps` `pytest` fixture) have more methods than the improved `driver` format. The regular formats also have more features. Some features, (such as the [PythonSelenium dashboard](/examples/example_logs/ReadMe.md)), require a `pytest` format.

--------

### ✅ No More Flaky Tests!

<p>PythonSelenium methods automatically wait for page elements to finish loading before interacting with them (<i>up to a timeout limit</i>). This means <b>you no longer need random <span><code>time.sleep()</code></span> statements</b> in your scripts.</p>

**There are three layers of protection that provide reliability for tests using PythonSelenium:**

* **(1)**: Selenium's default ``pageLoadStrategy`` is ``normal``: This strategy causes Selenium to wait for the full page to load, with HTML content and sub-resources downloaded and parsed.

* **(2)**: PythonSelenium includes methods such as ``wait_for_ready_state_complete()``, which run inside other PythonSelenium methods to ensure that it's safe to proceed with the next command.

* **(3)**: PythonSelenium methods automatically wait for elements to be visible and interactable before interacting with those elements.

**If you want to speed up your tests and you think the third level of protection is enough by itself, you can use command-line options to remove the first, the second, or both of those first two levels of protection:**

* ``--pls=none`` --> Set ``pageLoadStrategy`` to ``"none"``: This strategy causes Selenium to return immediately after the initial HTML content is fully received by the browser.

* ``--sjw`` --> Skip JS Waits, such as ``wait_for_ready_state_complete()``.

--------
