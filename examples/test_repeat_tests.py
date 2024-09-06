""" Tests to demonstrate how to repeat the same test multiple times.
    The 1st example uses the "parameterized" library.
    The 2nd example uses "pytest.mark.parametrize()". (NO class)
    The 3rd example uses "pytest.mark.parametrize()". (in class) """

import pytest
from parameterized import parameterized

from pythonselenium import BaseCase

BaseCase.main(__name__, __file__, "-n6")

url = "data:text/html,<h2>Hello</h2><p><input />&nbsp;<button>OK!</button></p>"


class RepeatTests(BaseCase):
    @parameterized.expand([[]] * 2)
    def test_repeat_this_test_with_parameterized(self):
        self.open(url)
        self.type("input", "PythonSelenium is fun")
        self.click('button:contains("OK!")')
        self.assert_text("Hello", "h2")


@pytest.mark.parametrize("", [[]] * 2)
def test_repeat_this_test_with_pytest_parametrize(ps):
    ps.open(url)
    ps.type("input", "PythonSelenium is fun")
    ps.click('button:contains("OK!")')
    ps.assert_text("Hello", "h2")


class RepeatTestsWithPytest:
    @pytest.mark.parametrize("", [[]] * 2)
    def test_repeat_test_with_pytest_parametrize(self, ps):
        ps.open(url)
        ps.type("input", "PythonSelenium is fun")
        ps.click('button:contains("OK!")')
        ps.assert_text("Hello", "h2")
