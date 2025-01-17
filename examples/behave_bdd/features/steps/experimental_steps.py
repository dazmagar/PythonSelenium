from behave import step

from pythonselenium.common.decorators import continue_on_fail


@step("Step without error")
def pass_method(context):
    pass

@step("Step with ignore error.")
@continue_on_fail
def ignore_error_method(context):
    tt = 1 / 0

@step("Step with error.")
def raise_error_method(context):
    raise AssertionError("Real error")
