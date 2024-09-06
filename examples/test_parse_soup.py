import re

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class SoupParsingTests(BaseCase):
    def click_menu_item(self, text):
        # Use BeautifulSoup to parse the selector ID from element text.
        # Then click on the element with the ID.
        # (This is useful when the selector ID is auto-generated.)
        pattern = re.compile(text)
        soup = self.get_beautiful_soup()
        the_id = soup.find(string=pattern).parent.parent.attrs["id"]
        self.click("#%s" % the_id)

    def test_beautiful_soup_parsing(self):
        self.open("https://www.quackit.com/html/html_editors/tinymce_editor.cfm")
        self.highlight("#tinymce-21")
        self.click_menu_item("File")
        self.click_menu_item("New document")
        self.click_menu_item("Formats")
        self.click_menu_item("Headings")
        self.click_menu_item("Heading 1")
        self.switch_to_frame("#mceEditor_ifr")
        self.add_text("#tinymce", "Automate anything with PythonSelenium!\n")
        self.switch_to_default_content()
        self.post_message("Learn PythonSelenium Today!")
