"""Classic Page Object Model with the "ps" fixture."""

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class DataPage:
    def go_to_data_url(self, ps):
        ps.open("data:text/html,<p>Hello!</p><input />")

    def add_input_text(self, ps, text):
        ps.type("input", text)


class ObjTests:
    def test_data_url_page(self, ps):
        DataPage().go_to_data_url(ps)
        ps.assert_text("Hello!", "p")
        DataPage().add_input_text(ps, "Goodbye!")
