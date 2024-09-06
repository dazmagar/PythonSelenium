import pytest


# Use the pytest "request" fixture to get the "ps" fixture (no class)
@pytest.mark.offline  # Can be run with: "pytest -m offline"
def test_request_fixture(request):
    ps = request.getfixturevalue("ps")
    ps.open("data:text/html,<p>Hello<br><input></p>")
    ps.assert_element("html > body")
    ps.assert_text("Hello", "body p")
    ps.type("input", "Goodbye")
    ps.click("body p")
    ps.tearDown()


# Use the pytest "request" fixture to get the "ps" fixture (in class)
@pytest.mark.offline
class RequestTests:
    def test_request_fixture_in_class(self, request):
        ps = request.getfixturevalue("ps")
        ps.open("data:text/html,<p>Hello<br><input></p>")
        ps.assert_element("html > body")
        ps.assert_text("Hello", "body p")
        ps.type("input", "Goodbye")
        ps.click("body p")
        ps.tearDown()
