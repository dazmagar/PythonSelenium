# isort: off
from behave.runner import Context
from behave.model import Step, Status

from pythonselenium import BaseCase
from pythonselenium.behave import behave_ps

behave_ps.set_base_class(BaseCase)  # Accepts a BaseCase subclass
from pythonselenium.behave.behave_ps import after_all  # noqa
from pythonselenium.behave.behave_ps import after_feature  # noqa
from pythonselenium.behave.behave_ps import after_scenario  # noqa
from pythonselenium.behave.behave_ps import after_step as origin_after_step  # noqa
from pythonselenium.behave.behave_ps import before_all as origin_before_all  # noqa
from pythonselenium.behave.behave_ps import before_feature  # noqa
from pythonselenium.behave.behave_ps import before_scenario  # noqa
from pythonselenium.behave.behave_ps import before_step  # noqa


def before_all(context: Context) -> None:
    origin_before_all(context)
    context.tmp_data = {}


def after_step(context: Context, step: Step) -> None:
    continue_on_fail = getattr(context, "current_step_continue_on_fail", False)
    if step.status == Status.failed and continue_on_fail:
        step.status = Status.skipped
        step.error_message = None
    context.current_step_continue_on_fail = False
    origin_after_step(context, step)
