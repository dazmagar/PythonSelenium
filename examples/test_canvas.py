"""Use PythonSelenium methods to interact with "canvas" elements."""

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


class CanvasTests(BaseCase):

    def get_pixel_colors(self, x=0, y=0):
        # Return the RGB colors of the canvas element's top left pixel
        if self.browser == "safari":
            x += 1
            y += 1

        color = self.execute_script("return document.querySelector('canvas').getContext('2d').getImageData(%s, %s, 1, 1).data;" % (x, y))

        if self.is_chromium():
            return [color[0], color[1], color[2]]
        else:
            return [color["0"], color["1"], color["2"]]

    def test_canvas_click_from_center(self):
        self.load_html_file("examples/offline_examples/canvas_page.html")
        self.assert_title_contains("Canvas")
        rgb = self.get_pixel_colors(3, 3)
        self.assert_equal(rgb, [0, 128, 128])  # teal - color of canvas
        self.click_with_offset("canvas", 0, 0, mark=True, center=True)
        self.sleep(0.55)  # Not needed (Lets you see the alert pop up)
        alert = self.switch_to_alert()
        self.assert_equal(alert.text, "You clicked on the square!")
        self.accept_alert()
        self.sleep(0.55)  # Not needed (Lets you see the alert go away)
        rgb = self.get_pixel_colors(290, 190)
        self.assert_equal(rgb, [225, 225, 225])  # gray - color of square inside canvas
        if self.browser == "safari" and self._reuse_session:
            # Alerts can freeze Safari if reusing the browser session
            self.driver.quit()
