from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class ScrapeBingTests(BaseCase):
    def test_scrape_bing(self):
        if self._multithreaded:
            self.open_if_not_url("about:blank")
            self.skip("Skipping test in multi-threaded mode.")
        self.open("www.bing.com/search?q=Selenium+GitHub&qs=n&form=QBRE")
        self.wait_for_element("main h2 a")
        soup = self.get_beautiful_soup()
        titles = [item.text for item in soup.select("main h2 a")]
        print("\nSearch Result Headers:")
        for title in titles:
            if "selenium/" in title.lower() or "Selenium" in title:
                print("    " + title)
        links = [item["href"] for item in soup.select("main h2 a")]
        print("Search Result Links:")
        for link in links:
            if "github.com/SeleniumHQ/selenium" in link.lower() or "https://www.selenium.dev/" in link.lower():
                print("    " + link)
        self.click_if_visible('a[href="https://github.com/SeleniumHQ/selenium"]')
        print("Last Page = " + self.get_current_url())
