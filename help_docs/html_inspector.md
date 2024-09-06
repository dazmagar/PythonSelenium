<!-- PythonSelenium Docs -->

## The HTML Inspector 🕵️

🕵️ <b>HTML Inspector</b> provides useful info about a web page.

🕵️ (<i>Based on: [github.com/philipwalton/html-inspector](https://github.com/philipwalton/html-inspector)</i>)

🕵️ Example: [examples/test_inspect_html.py](/examples/test_inspect_html.py) (Chromium-only)

```python
from pythonselenium import BaseCase
BaseCase.main(__name__, __file__)

class HtmlInspectorTests(BaseCase):
    def test_html_inspector(self):
        self.open("https://xkcd.com/1144/")
        self.inspect_html()
```

--------

```bash
pytest test_inspect_html.py
============== test session starts ==============

* HTML Inspection Results: https://xkcd.com/1144/
⚠️  'property' is not a valid attribute of the <meta> element.
⚠️  Do not use <div> or <span> elements without any attributes.
⚠️  'srcset' is not a valid attribute of the <img> element.
⚠️  The 'border' attribute is no longer valid on the <img> element.
⚠️  The <center> element is obsolete.
⚠️  The id 'comicLinks' appears more than once in the document.
* (See the Console output for details!)
```
