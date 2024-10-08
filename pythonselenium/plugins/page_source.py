"""PageSource Plugin for PythonSelenium tests that run with pynose / nosetests"""
import os
import codecs
from nose.plugins import Plugin
from pythonselenium.config import settings
from pythonselenium.core import log_helper


class PageSource(Plugin):
    """Capture the page source after a test fails."""
    name = "page_source"  # Usage: --with-page_source
    logfile_name = settings.PAGE_SOURCE_NAME

    def options(self, parser, env):
        super().options(parser, env=env)

    def configure(self, options, conf):
        super().configure(options, conf)
        if not self.enabled:
            return
        self.options = options

    def addError(self, test, err, capt=None):
        try:
            page_source = test.driver.page_source
        except Exception:
            return
        test_logpath = self.options.log_path + "/" + test.id()
        if not os.path.exists(test_logpath):
            os.makedirs(test_logpath)
        html_file_name = os.path.join(test_logpath, self.logfile_name)
        html_file = codecs.open(html_file_name, "w+", "utf-8")
        rendered_source = log_helper.get_html_source_with_base_href(
            test.driver, page_source
        )
        html_file.write(rendered_source)
        html_file.close()

    def addFailure(self, test, err, capt=None, tbinfo=None):
        try:
            page_source = test.driver.page_source
        except Exception:
            return
        test_logpath = self.options.log_path + "/" + test.id()
        if not os.path.exists(test_logpath):
            os.makedirs(test_logpath)
        html_file_name = os.path.join(test_logpath, self.logfile_name)
        html_file = codecs.open(html_file_name, "w+", "utf-8")
        rendered_source = log_helper.get_html_source_with_base_href(
            test.driver, page_source
        )
        html_file.write(rendered_source)
        html_file.close()
