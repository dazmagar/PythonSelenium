"""DriverContext() example. (Runs with "python")."""

from pythonselenium import DriverContext

with DriverContext(browser="chrome", incognito=True) as driver:
    driver.open("https://github.com/search")
    driver.highlight(".octicon-logo-github:first-of-type", loops=6)
    driver.type("input[aria-label*='Search']", "selenium")
    driver.highlight("input[aria-label*='Search']", loops=6)
