from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class GitHubTests(BaseCase):
    def test_github(self):
        if self.headless or self.page_load_strategy == "none":
            self.open_if_not_url("about:blank")
            print("\n  Unsupported mode for this test.")
            self.skip("Unsupported mode for this test.")
        self.open("https://github.com/SeleniumHQ/selenium")
        self.click_if_visible('[data-action="click:signup-prompt#dismiss"]')
        self.highlight("div.Layout-main")
        self.highlight("div.Layout-sidebar")
        self.assert_element("div.repository-content")
        self.assert_text("selenium", "strong a")
        self.js_click("div.Layout-sidebar a[title='https://selenium.dev']")
        self.slow_click("li a:contains('Downloads')")
        self.assert_element("h1:contains('Downloads')")
