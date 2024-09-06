<!-- PythonSelenium Docs -->

## ✅ Support for migrating from raw Selenium to PythonSelenium

### 🔵 Here are some examples that can help you understand how to migrate from raw Selenium to PythonSelenium

The five main examples in the [examples/migration/raw_selenium](/examples/migration/raw_selenium) folder are:

* [flaky_messy_raw.py](/examples/migration/raw_selenium/flaky_messy_raw.py)
* [long_messy_raw.py](/examples/migration/raw_selenium/long_messy_raw.py)
* [messy_raw.py](/examples/migration/raw_selenium/messy_raw.py)
* [refined_raw.py](/examples/migration/raw_selenium/refined_raw.py)
* [simple_pysel.py](/examples/migration/raw_selenium/simple_pysel.py)

Each of these examples is structured as a test that can be run with ``pytest``. They all inherit ``unittest.TestCase`` either directly, or via ``pythonselenium.BaseCase``, which extends it. This provides automatically-called ``setUp()`` and ``tearDown()`` methods before and after each test.

> These examples show the evolution of tests from raw Selenium to PythonSelenium. By understanding common progressions of Selenium engineers, you can avoid making the same mistakes as they did, and learn to write good tests efficiently without the long learning curve.

* [flaky_messy_raw.py](/examples/migration/raw_selenium/flaky_messy_raw.py)

> This is common example of how newcomers to Selenium write tests (assuming they've already learned how to break out reusuable code into ``setUp()`` and ``tearDown()`` methods). It uses ``find_element()`` calls, which can lead to flaky tests because those calls fail if a page element is slow to load.

* [long_messy_raw.py](/examples/migration/raw_selenium/long_messy_raw.py)

> At the next stage of learning, newcomers to Selenium realize that their tests are flaky, so they start replacing existing ``find_element()`` calls with ``WebDriverWait`` and internal Selenium ``expected_conditions`` methods, such as ``visibility_of_element_located`` and ``element_to_be_clickable``. This can result in long/messy tests that are unmaintainable if not written carefully.

* [messy_raw.py](/examples/migration/raw_selenium/messy_raw.py)

> By this stage, newcomers to Selenium have evolved into legitimate test automation engineers. They have become better at writing reusable code, so they've broken down the long ``WebDriverWait`` and ``expected_conditions`` calls into shorter method calls, which are easier to read, but could still be improved on for better maintainability. Here, individual page actions are still written out as multiple lines of code, (or multiple method calls per line), which isn't efficient.

* [refined_raw.py](/examples/migration/raw_selenium/refined_raw.py)

> By now, the test automation engineer has become an expert in breaking out code into reusable methods, and the test itself has been simplified down to a single page action per line. The code is easy to read and easy to maintain. The error output is also simplified. The journey of writing a complete test automation framework for Selenium has begun.

* [simple_pysel.py](/examples/migration/raw_selenium/simple_pysel.py)

With a complete test automation framework built, most of the hard work is already done for you. By importing ``BaseCase`` into your test classes, your tests gain access to all PythonSelenium methods, which can simplify your code. PythonSelenium also provides a lot of additional functionality that isn't included with raw Selenium.


### 🔵 How is PythonSelenium different from raw Selenium?

<div>

<p>💡 PythonSelenium is a Python framework for browser automation and testing. PythonSelenium uses <a href="https://www.w3.org/TR/webdriver2/#endpoints" target="_blank">Selenium/WebDriver</a> APIs and incorporates test-runners such as <code>pytest</code>, <code>pynose</code>, and <code>behave</code> to provide organized structure, test discovery, test execution, test state (<i>eg. passed, failed, or skipped</i>), and command-line options for changing default settings (<i>eg. browser selection</i>). With raw Selenium, you would need to set up your own options-parser for configuring tests from the command-line.</p>

<p>💡 PythonSelenium's driver manager gives you more control over automatic driver downloads. (Use <code>--driver-version=VER</code> with your <code>pytest</code> run command to specify the version.) By default, PythonSelenium will download a driver version that matches your major browser version if not set.</p>

<p>💡 PythonSelenium automatically detects between CSS Selectors and XPath, which means you don't need to specify the type of selector in your commands (<i>but optionally you could</i>).</p>

<p>💡 PythonSelenium methods often perform multiple actions in a single method call. For example, <code>self.type(selector, text)</code> does the following:<br />1. Waits for the element to be visible.<br />2. Waits for the element to be interactive.<br />3. Clears the text field.<br />4. Types in the new text.<br />5. Presses Enter/Submit if the text ends in <code>"\n"</code>.<br />With raw Selenium, those actions require multiple method calls.</p>

<p>💡 PythonSelenium uses default timeout values when not set:<br />
✅ <code>self.click("button")</code><br />
With raw Selenium, methods would fail instantly (<i>by default</i>) if an element needed more time to load:<br />
❌ <code>self.driver.find_element(by="css selector", value="button").click()</code><br />
(Reliable code is better than unreliable code.)</p>

<p>💡 PythonSelenium lets you change the explicit timeout values of methods:<br />
✅ <code>self.click("button", timeout=10)</code><br />
With raw Selenium, that requires more code:<br />
❌ <code>WebDriverWait(driver, 10).until(EC.element_to_be_clickable("css selector", "button")).click()</code><br />
(Simple code is better than complex code.)</p>

<p>💡 PythonSelenium gives you clean error output when a test fails. With raw Selenium, error messages can get very messy.</p>

<p>💡 PythonSelenium gives you the option to generate a dashboard and reports for tests. It also saves screenshots from failing tests to the <code>./latest_logs/</code> folder. Raw <a href="https://www.selenium.dev/documentation/webdriver/" target="_blank">Selenium</a> does not have these options out-of-the-box.</p>

<p>💡 PythonSelenium includes desktop GUI apps for running tests, such as <a href="">PythonSelenium Commander</a> for <code>pytest</code> and <a href="">PythonSelenium Behave GUI</a> for <code>behave</code>.</p>

<p>💡 PythonSelenium has its own <a href="">Recorder / Test Generator</a> for creating tests from manual browser actions.</p>

<p>💡 PythonSelenium comes with <a href="">test case management software, ("Case Plans")</a>, for organizing tests and step descriptions.</p>

<p>💡 PythonSelenium includes tools for <a href="">building data apps, ("Chart Maker")</a>, which can generate JavaScript from Python.</p>

</div>

--------
