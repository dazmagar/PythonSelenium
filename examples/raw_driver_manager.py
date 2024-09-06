"""Driver() manager example. (Runs with "python")."""

from pythonselenium import Driver

driver = Driver(browser="chrome", headless=False)
try:
    driver.open("https://github.com/search")
    driver.highlight(".octicon-logo-github:first-of-type", loops=6)
    driver.type("input[aria-label*='Search']", "selenium")
    driver.highlight("input[aria-label*='Search']", loops=6)
finally:
    driver.quit()
