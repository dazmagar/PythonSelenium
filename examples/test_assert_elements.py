"""Assert that multiple elements are present or visible:
HTML Presence: assert_elements_present()
HTML Visibility: assert_elements() <> assert_elements_visible()"""

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class ListAssertTests(BaseCase):
    def test_assert_list_of_elements(self):
        self.load_html_file("examples/offline_examples/demo_page.html")
        self.assert_elements_present("head", "style", "script")
        self.assert_elements("h1", "h2", "h3")
        my_list = ["#myDropdown", "#myButton", "#mySlider"]
        self.assert_elements(my_list)
        self.wait(3)
