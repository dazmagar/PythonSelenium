import collections
import os
import pdb
try:
    import pdbp  # (Pdb+) --- Python Debugger Plus
except Exception:
    pass
import sys
from selenium import webdriver
from pythonselenium.__version__ import __version__
from pythonselenium.common import decorators  # noqa
from pythonselenium.common import encryption  # noqa
from pythonselenium.core import colored_traceback
from pythonselenium.core.browser_launcher import get_driver  # noqa
from pythonselenium.fixtures import js_utils  # noqa
from pythonselenium.fixtures import page_actions  # noqa
from pythonselenium.fixtures import page_utils  # noqa
from pythonselenium.fixtures import shared_utils  # noqa
from pythonselenium.fixtures.base_case import BaseCase  # noqa
from pythonselenium.masterqa.master_qa import MasterQA  # noqa
from pythonselenium.plugins.ps_manager import PS  # noqa
from pythonselenium.plugins.driver_manager import Driver  # noqa
from pythonselenium.plugins.driver_manager import DriverContext  # noqa

if sys.version_info[0] < 3 and "pdbp" in locals():
    # With Python3, "import pdbp" is all you need
    for key in pdbp.__dict__.keys():
        # Replace pdb with pdbp
        pdb.__dict__[key] = pdbp.__dict__[key]
    if hasattr(pdb, "DefaultConfig"):
        # Here's how to customize Pdb+ options
        pdb.DefaultConfig.filename_color = pdb.Color.fuchsia
        pdb.DefaultConfig.line_number_color = pdb.Color.turquoise
        pdb.DefaultConfig.truncate_long_lines = False
        pdb.DefaultConfig.sticky_by_default = True
colored_traceback.add_hook()
os.environ["SE_AVOID_STATS"] = "true"  # Disable Selenium Manager stats
if sys.version_info >= (3, 7):
    webdriver.TouchActions = None  # Lifeline for past selenium-wire versions
if sys.version_info >= (3, 10):
    collections.Callable = collections.abc.Callable  # Lifeline for nosetests
del collections  # Undo "import collections" / Simplify "dir(pythonselenium)"
del os  # Undo "import os" / Simplify "dir(pythonselenium)"
del sys  # Undo "import sys" / Simplify "dir(pythonselenium)"
del webdriver  # Undo "import webdriver" / Simplify "dir(pythonselenium)"

version_list = [int(i) for i in __version__.split(".") if i.isdigit()]
version_tuple = tuple(version_list)
version_info = version_tuple  # noqa
