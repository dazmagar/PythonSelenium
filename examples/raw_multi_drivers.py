import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from random import randint, seed

from pythonselenium import Driver

sys.argv.append("-n")  # Tell PythonSelenium to do thread-locking as needed


def launch_driver(url):
    seed(len(threading.enumerate()))  # Random seed for browser placement
    driver = Driver()
    try:
        driver.set_window_rect(randint(4, 720), randint(8, 410), 700, 500)
        driver.get(url=url)
        if driver.is_element_visible("main h1"):
            driver.highlight("main h1", loops=9)
        else:
            driver.sleep(2.2)
    finally:
        driver.quit()


if __name__ == "__main__":
    urls = ["https://wikipedia.org" for i in range(4)]
    with ThreadPoolExecutor(max_workers=len(urls)) as executor:
        for url in urls:
            executor.submit(launch_driver, url)
