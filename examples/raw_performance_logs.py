from rich.pretty import pprint

from pythonselenium import PS

with PS(log_cdp=True) as ps:
    ps.open("wikipedia.org")
    ps.sleep(1)
    pprint(ps.driver.get_log("performance"))
