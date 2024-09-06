from pythonselenium import BaseCase

BaseCase.main(__name__, __file__)


# Use the pytest "request" fixture to get the "ps" fixture (no class)
def test_request_ps_fixture(request):
    ps = request.getfixturevalue("ps")
    ps.load_html_file("examples/offline_examples/demo_page.html")
    ps.assert_text("PythonSelenium", "#myForm h2")
    ps.assert_element("input#myTextInput")
    ps.type("#myTextarea", "This is me")
    ps.click("#myButton")
    ps.tearDown()


# Use the pytest "request" fixture to get the "ps" fixture (in class)
class Test_Request_Fixture:
    def test_request_ps_fixture_in_class(self, request):
        ps = request.getfixturevalue("ps")
        ps.load_html_file("examples/offline_examples/demo_page.html")
        ps.assert_element("input#myTextInput")
        ps.type("#myTextarea", "Automated")
        ps.assert_text("This Text is Green", "#pText")
        ps.click("#myButton")
        ps.assert_text("This Text is Purple", "#pText")
        ps.tearDown()
