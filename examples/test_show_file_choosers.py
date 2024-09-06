"""self.show_file_choosers() is used to show hidden file-upload fields.
Verify that one can choose a file after the hidden input is visible."""

import os

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class FileUpload(BaseCase):
    def test_show_file_choosers(self):
        self.open("https://imgbb.com/")
        self.wait_for_element('img[alt="ImgBB"]')
        choose_file_selector = "#anywhere-upload-input"
        uploaded_image = "#anywhere-upload-queue li.queue-item"
        self.assert_element_not_visible(choose_file_selector)
        self.show_file_choosers()
        self.assert_element_not_visible(uploaded_image)
        dir_name = os.path.dirname(os.path.abspath(__file__))
        my_file = "screenshot.png"
        file_path = os.path.join(dir_name, "example_logs/%s" % my_file)
        self.choose_file(choose_file_selector, file_path)
        if self.browser != "safari":
            seen_path = "%s\\%s" % ("C:\\fakepath", my_file)
            self.assert_attribute(choose_file_selector, "value", seen_path)
        self.demo_mode = True
        self.assert_element(uploaded_image)
