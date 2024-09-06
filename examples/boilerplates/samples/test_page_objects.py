"""An example using the Classic Page Object Model."""

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class GooglePage:
    def go_to_google(self, ps):
        ps.open("https://google.com/ncr")

    def assert_google_title(self, ps):
        ps.assert_title_contains("Google")

    def hide_sign_in_pop_up(self, ps):
        if not ps.is_element_visible("iframe"):
            ps.sleep(1.5)  # A slow pop-up might appear
        ps.hide_elements("iframe")
        ps.sleep(0.05)

    def do_search(self, ps, search_term):
        ps.sleep(0.05)
        ps.click('[title="Search"]')
        ps.type('[title="Search"]', search_term + "\n")

    def click_search_result(self, ps, content):
        ps.click('a:contains("%s")' % content)


class SeleniumPage:
    def go_navigation(self, ps, nav_item):
        ps.sleep(0.05)
        ps.click("ul li:contains(%s)" % nav_item)


class MyTests(BaseCase):
    def test_page_objects(self):
        if self.headless and self._multithreaded:
            self.open_if_not_url("about:blank")
            print("\n  Skipping test in headless multi-threaded mode.")
            self.skip("Skipping test in headless multi-threaded mode.")
        search_term = "selenium.dev"
        expected_text = "Selenium"
        GooglePage().go_to_google(self)
        GooglePage().assert_google_title(self)
        GooglePage().hide_sign_in_pop_up(self)
        GooglePage().do_search(self, search_term)
        self.assert_text(expected_text, "#search")
        GooglePage().click_search_result(self, expected_text)
        SeleniumPage().go_navigation(self, "Downloads")
        self.assert_text("Downloads", "main h1")
