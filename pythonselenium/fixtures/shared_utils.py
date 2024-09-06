"""Shared utility methods"""

import os
import platform
import sys
import time

from pythonselenium import config as ps_config
from pythonselenium.fixtures import constants


def pip_install(package, version=None):
    import subprocess

    import fasteners

    pip_install_lock = fasteners.InterProcessLock(constants.PipInstall.LOCKFILE)
    with pip_install_lock:
        if not version:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        else:
            package_and_version = package + "==" + str(version)
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_and_version])


def is_arm_mac():
    """(M1 / M2 Macs use the ARM processor)"""
    return "darwin" in sys.platform and ("arm" in platform.processor().lower() or "arm64" in platform.version().lower())


def is_mac():
    return "darwin" in sys.platform


def is_linux():
    return "linux" in sys.platform


def is_windows():
    return "win32" in sys.platform


def is_safari(driver):
    return driver.capabilities["browserName"].lower() == "safari"


def get_terminal_width():
    width = 80  # default
    try:
        width = os.get_terminal_size().columns
    except Exception:
        try:
            import shutil

            width = shutil.get_terminal_size((80, 20)).columns
        except Exception:
            pass
    return width


def format_exc(exception, message):
    """Formats an exception message to make the output cleaner."""
    from selenium.common.exceptions import (
        ElementNotVisibleException,
        NoAlertPresentException,
        NoSuchAttributeException,
        NoSuchElementException,
        NoSuchFrameException,
        NoSuchWindowException,
    )

    from pythonselenium.common import exceptions
    from pythonselenium.common.exceptions import (
        LinkTextNotFoundException,
        NoSuchFileException,
        NoSuchOptionException,
        TextNotVisibleException,
    )

    if exception is Exception:
        exc = Exception
        return exc, message
    elif exception is ElementNotVisibleException:
        exc = exceptions.ElementNotVisibleException
    elif exception == "ElementNotVisibleException":
        exc = exceptions.ElementNotVisibleException
    elif exception is LinkTextNotFoundException:
        exc = exceptions.LinkTextNotFoundException
    elif exception == "LinkTextNotFoundException":
        exc = exceptions.LinkTextNotFoundException
    elif exception is NoSuchElementException:
        exc = exceptions.NoSuchElementException
    elif exception == "NoSuchElementException":
        exc = exceptions.NoSuchElementException
    elif exception is TextNotVisibleException:
        exc = exceptions.TextNotVisibleException
    elif exception == "TextNotVisibleException":
        exc = exceptions.TextNotVisibleException
    elif exception is NoAlertPresentException:
        exc = exceptions.NoAlertPresentException
    elif exception == "NoAlertPresentException":
        exc = exceptions.NoAlertPresentException
    elif exception is NoSuchAttributeException:
        exc = exceptions.NoSuchAttributeException
    elif exception == "NoSuchAttributeException":
        exc = exceptions.NoSuchAttributeException
    elif exception is NoSuchFrameException:
        exc = exceptions.NoSuchFrameException
    elif exception == "NoSuchFrameException":
        exc = exceptions.NoSuchFrameException
    elif exception is NoSuchWindowException:
        exc = exceptions.NoSuchWindowException
    elif exception == "NoSuchWindowException":
        exc = exceptions.NoSuchWindowException
    elif exception is NoSuchFileException:
        exc = exceptions.NoSuchFileException
    elif exception == "NoSuchFileException":
        exc = exceptions.NoSuchFileException
    elif exception is NoSuchOptionException:
        exc = exceptions.NoSuchOptionException
    elif exception == "NoSuchOptionException":
        exc = exceptions.NoSuchOptionException
    elif isinstance(exception, str):
        exc = Exception
        message = "%s: %s" % (exception, message)
        return exc, message
    else:
        exc = Exception
        return exc, message
    message = _format_message(message)
    try:
        exc.message = message
    except Exception:
        pass
    return exc, message


def _format_message(message):
    message = "\n " + message
    return message


def __time_limit_exceeded(message):
    from pythonselenium.common.exceptions import TimeLimitExceededException

    raise TimeLimitExceededException(message)


def check_if_time_limit_exceeded():
    if hasattr(ps_config, "time_limit") and ps_config.time_limit and not ps_config.recorder_mode:
        time_limit = ps_config.time_limit
        now_ms = int(time.time() * 1000)
        if now_ms > ps_config.start_time_ms + ps_config.time_limit_ms:
            display_time_limit = time_limit
            plural = "s"
            if float(int(time_limit)) == float(time_limit):
                display_time_limit = int(time_limit)
                if display_time_limit == 1:
                    plural = ""
            message = "This test has exceeded the time limit of %s second%s!" % (display_time_limit, plural)
            message = _format_message(message)
            __time_limit_exceeded(message)
