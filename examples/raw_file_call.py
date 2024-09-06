"""Call a file with "python" instead of "pytest" directly.
Added pytest args from the command-line won't be included.
To run, use: "python raw_file_call.py"."""

from pythonselenium import BaseCase

if __name__ == "__main__":
    from pytest import main

    main([__file__, "-s"])


class TinyMceTest(BaseCase):
    def test_tinymce(self):
        self.open("https://codepen.io/tinymce/live/QWNpjbg")
        iframe1 = self.locator("iframe[id='result']")
        with self.frame_switch(iframe1):
            self.click('span:contains("File")')
            self.click('div[title="New document"]')
            self.click('button:contains("Format")')
            self.click('div[title="Formats"]')
            self.click('div[title="Headings"]')
            self.click('div[title="Heading 1"]')
            iframe2 = self.locator("iframe[id='mytextarea_ifr']")
            with self.frame_switch(iframe2):
                self.add_text("#tinymce", "PythonSelenium!")
                self.highlight("#tinymce")
                self.post_message("PythonSelenium is fast!", duration=1.5)
