<!-- PythonSelenium Docs -->

## Installing webdrivers

To run web automation, you'll need webdrivers for each browser you plan on using.  With PythonSelenium, drivers are downloaded automatically as needed into the PythonSelenium ``drivers`` folder.

You can also download drivers manually with these commands:

```bash
pythonselenium get chromedriver
pythonselenium get geckodriver
pythonselenium get edgedriver
```

After running the commands above, web drivers will get downloaded into the ``pythonselenium/drivers/`` folder. PythonSelenium uses those drivers during tests. (The drivers don't come with PythonSelenium by default.)

If the necessary driver is not found in this location while running tests, PythonSelenium will instead look for the driver on the System PATH. If the necessary driver is not on the System PATH either, PythonSelenium will automatically attempt to download the required driver.

* You can also download specific versions of drivers. Examples:

```bash
pysel get chromedriver 114
pysel get chromedriver 114.0.5735.90
pysel get chromedriver stable
pysel get chromedriver beta
pysel get chromedriver dev
pysel get chromedriver canary
pysel get chromedriver previous  # One major version before the stable version
pysel get chromedriver mlatest  # Milestone latest version for detected browser
pysel get edgedriver 115.0.1901.183
```

(NOTE: ``pysel`` is a shortcut for ``pythonselenium``)

--------

If you plan on using the [Selenium Grid integration](/pythonselenium/utilities/selenium_grid/ReadMe.md) (which allows for ``remote`` webdriver), you'll need to put the drivers on your System PATH. On macOS and Linux, ``/usr/local/bin`` is a good PATH spot. On Windows, you may need to set the System PATH under Environment Variables to include the location where you placed the driver files. As a shortcut, you could place the driver files into your Python ``Scripts/`` folder in the location where you have Python installed, which should already be on your System PATH.

Here's where you can go to manually get web drivers from the source:

* For Chrome, get [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) on your System PATH.

* For Edge, get [Edge Driver (Microsoft WebDriver)](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) on your System PATH.

* For Firefox, get [Geckodriver](https://github.com/mozilla/geckodriver/releases) on your System PATH.

* For Safari, get [Safari Driver](/help_docs/using_safari_driver.md) on your System PATH.

**macOS shortcuts**:

* You can also install drivers by using ``brew`` (aka ``homebrew``):

```bash
brew install --cask chromedriver

brew install geckodriver
```

You can also upgrade existing webdrivers:

```bash
brew upgrade --cask chromedriver

brew upgrade geckodriver
```

**Linux shortcuts**:

If you still need drivers, these scripts download ``chromedriver`` and ``geckodriver`` to a Linux machine:

```bash
wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver /usr/local/bin/
chmod +x /usr/local/bin/chromedriver
```

```bash
wget https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz
tar xvfz geckodriver-v0.34.0-linux64.tar.gz
mv geckodriver /usr/local/bin/
chmod +x /usr/local/bin/geckodriver
```

To verify that web drivers are working, **[follow these instructions](/help_docs/verify_webdriver.md)**.
