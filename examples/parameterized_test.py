from parameterized import parameterized

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class SearchTests(BaseCase):

    @parameterized.expand(["United States", "Black hole"])
    def test_parameterized_search(self, search_term):
        self.open("https://en.wikipedia.org/wiki/Special:Search")
        self.assert_title_contains("Search - Wikipedia")
        self.type("input[id='ooui-php-1']", search_term + "\n")
        self.assert_text(search_term, f".searchResultImage-text a[title='{search_term}']")
        self.wait(1)
