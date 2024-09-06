from pythonselenium import BaseCase
from pythonselenium.behave import behave_ps

behave_ps.set_base_class(BaseCase)  # Accepts a BaseCase subclass
from pythonselenium.behave.behave_ps import after_all  # noqa
from pythonselenium.behave.behave_ps import after_feature  # noqa
from pythonselenium.behave.behave_ps import after_scenario  # noqa
from pythonselenium.behave.behave_ps import after_step  # noqa
from pythonselenium.behave.behave_ps import before_all  # noqa
from pythonselenium.behave.behave_ps import before_feature  # noqa
from pythonselenium.behave.behave_ps import before_scenario  # noqa
from pythonselenium.behave.behave_ps import before_step  # noqa
