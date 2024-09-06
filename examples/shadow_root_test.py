"""Piercing through shadow-root elements with the "::shadow" selector.
To confirm that "::shadow" works, print text and assert exact text."""

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class ShadowRootTest(BaseCase):
    def test_shadow_root(self):
        if self.recorder_mode or not self.is_chromium():
            self.open_if_not_url("about:blank")
            print("\n  Unsupported mode for this test.")
            self.skip("Unsupported mode for this test.")
        self.open("https://books-pwakit.appspot.com/explore?q=")

        search_book_input = "book-app::shadow book-input-decorator input[id='input']"
        self.type(search_book_input, "Sun Tzu The Art Of War\n")
        item = "book-app::shadow main book-explore::shadow ul li:nth-of-type(%s) "
        book_item = item + "book-item::shadow "
        book_item_title = book_item + "h2"
        self.assert_exact_text("The Art of War", book_item_title % "1")
        self.click(item % "1")

        detailed_item = "book-app::shadow book-detail::shadow "
        detailed_item_title = detailed_item + "h2"
        self.assert_exact_text("The Art of War", detailed_item_title)
        self.wait(3)
