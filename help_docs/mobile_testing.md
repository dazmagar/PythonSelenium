<!-- PythonSelenium Docs -->

## Mobile Mode / Mobile Testing

Use ``--mobile`` to run PythonSelenium tests using Chrome's mobile device emulator with default values for Device Metrics and User-Agent.

<b>Here's an example mobile test:</b>

[PythonSelenium/examples/test_skype_site.py](/examples/test_skype_site.py)

```bash
pytest test_skype_site.py --mobile
```

To configure Device Metrics, use:

```bash
--metrics="CSS_Width,CSS_Height,Pixel_Ratio"
```

To configure the User-Agent, use:

```bash
--agent="USER-AGENT-STRING"
```

To find real values for Device Metrics, see:

* [Device Metrics List](https://gist.github.com/sidferreira/3f5fad525e99b395d8bd882ee0fd9d00)

To find real User-Agent strings, see:

* [User Agent Strings List](https://developers.whatismybrowser.com/useragents/explore/)

--------

<b>Here's another example of a mobile test:</b>

[PythonSelenium/examples/test_swag_labs.py](/examples/test_swag_labs.py)

```bash
pytest test_swag_labs.py --mobile
```

<b>Here's an example of configuring mobile settings for that test:</b>

```bash
# Run tests using Chrome's mobile device emulator (default settings)
pytest test_swag_labs.py --mobile

# Run mobile tests specifying CSS Width, CSS Height, and Pixel-Ratio
pytest test_swag_labs.py --mobile --metrics="360,640,2"

# Run mobile tests specifying the user agent
pytest test_swag_labs.py --mobile --agent="Mozilla/5.0 (Linux; Android 9; Pixel 3 XL)"
```

--------

For some [PythonSelenium Syntax Formats](/help_docs/syntax_formats.md), you can also use `mobile=True` to run tests in Mobile Mode:

```python
from pythonselenium import Driver

driver = Driver(mobile=True)
try:
    driver.open("https://www.skype.com/en/get-skype/")
    driver.assert_element('[aria-label="Microsoft"]')
    driver.assert_text("Download Skype", "h1")
    driver.highlight("div.appBannerContent")
    driver.highlight("h1")
    driver.assert_text("Skype for Mobile", "h2")
    driver.highlight("h2")
    driver.highlight("#get-skype-0")
    driver.highlight_click("span[data-dropdown-icon]")
    driver.highlight("#get-skype-0_android-download")
    driver.highlight('[data-bi-id*="ios"]')
finally:
    driver.quit()
```

--------
