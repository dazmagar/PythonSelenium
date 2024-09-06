<!-- PythonSelenium Docs -->

## JS Package Manager and Code Generators

<h3>🕹️ PythonSelenium lets you load JavaScript packages from any CDN link into any website via Python.</h3>

<b>🎨 The following PythonSelenium solutions utilize this feature:</b>

🎦 [Demo Mode](/help_docs/demo_mode.md)

🚎 [Website Tours](/examples/tour_examples/ReadMe.md)

📊 [Chart Maker](/examples/chart_maker/ReadMe.md)

🛂 [Dialog Boxes](/examples/dialog_boxes/ReadMe.md)

--------

<p><div>🗺️ Here's an example of loading a website-tour library into the browser for a Google Maps tour:</div></p>

🗺️ This example is from [maps_introjs_tour.py](/examples/tour_examples/maps_introjs_tour.py) (The <code>--interval=1</code> makes the tour go automatically to the next step after 1 second.)

```bash
cd examples/tour_examples
pytest maps_introjs_tour.py --interval=1
```

<p>🕹️ PythonSelenium includes powerful JS code generators for converting Python into JavaScript for using the supported JS packages. A few lines of Python in your tests might generate hundreds of lines of JavaScript.</p>

🗺️ Here is some tour code in Python from [maps_introjs_tour.py](/examples/tour_examples/maps_introjs_tour.py) that expands into a lot of JavaScript.

```python
self.open("https://www.google.com/maps/@42.3591234,-71.0915634,15z")
self.create_tour(theme="introjs")
self.add_tour_step("Welcome to Google Maps!", title="PythonSelenium Tours")
self.add_tour_step("Enter Location", "#searchboxinput", title="Search Box")
self.add_tour_step("See it", "#searchbox-searchbutton", alignment="bottom")
self.add_tour_step("Thanks for using Tours!", title="End of Guided Tour")
self.export_tour(filename="maps_introjs_tour.js")
self.play_tour()
```

<p><div>🕹️ For existing features, PythonSelenium already takes care of loading all the necessary JS and CSS files into the web browser. To load other packages, here are a few useful methods that you should know about:</div></p>

```python
self.add_js_link(js_link)
```

<p><div>🕹️ This example loads the <a href="https://introjs.com/IntroJS</a> JavaScript library:</div></p>

```python
self.add_js_link("https://cdnjs.cloudflare.com/ajax/libs/intro.js/2.9.3/intro.min.js")
```

<div>🕹️ You can load any JS package this way as long as you know the URL.</div>

🕹️ If you're wondering how PythonSelenium does this, here's the full Python code from [js_utils.py](/pythonselenium/fixtures/js_utils.py), which uses WebDriver's <code>execute_script()</code> method for making JS calls after escaping quotes with backslashes as needed:

```python
def add_js_link(driver, js_link):
    script_to_add_js = (
        """function injectJS(link) {
              var body = document.getElementsByTagName("body")[0];
              var script = document.createElement("script");
              script.src = link;
              script.defer;
              script.type="text/javascript";
              script.crossorigin = "anonymous";
              script.onload = function() { null };
              body.appendChild(script);
           }
           injectJS("%s");""")
    js_link = escape_quotes_if_needed(js_link)
    driver.execute_script(script_to_add_js % js_link)
```

<p>🕹️ Now that you've loaded JavaScript into the browser, you may also want to load some CSS to go along with it:</p>

```python
self.add_css_link(css_link)
```

<p>🕹️ Here's code that loads the <a href="https://introjs.com/IntroJS</a> CSS:</p>

```python
self.add_css_link("https://cdnjs.cloudflare.com/ajax/libs/intro.js/2.9.3/introjs.css")
```

<p>🕹️ And here's the Python WebDriver code that makes this possible:</p>

```python
def add_css_link(driver, css_link):
    script_to_add_css = (
        """function injectCSS(css) {
              var head = document.getElementsByTagName("head")[0];
              var link = document.createElement("link");
              link.rel = "stylesheet";
              link.type = "text/css";
              link.href = css;
              link.crossorigin = "anonymous";
              head.appendChild(link);
           }
           injectCSS("%s");""")
    css_link = escape_quotes_if_needed(css_link)
    driver.execute_script(script_to_add_css % css_link)
```

<div>🕹️ Website tours are just one of the many uses of the JS Package Manager.</div>
<p><div>🛂 The following example shows the <a href="https://github.com/craftpip/jquery-confirm">JqueryConfirm</a> package loaded into a website for creating fancy dialog boxes:</div></p>

↕️ Example: [dialog_box_tour.py](/examples/dialog_boxes/dialog_box_tour.py) ↕️

<h4>Here's how to run that example:</h4>

```bash
cd examples/dialog_boxes
pytest test_dialog_boxes.py
```

Example from the [Dialog Boxes ReadMe](/examples/dialog_boxes/ReadMe.md)

<div>🕹️ Since packages are loaded directly from a CDN link, you won't need other package managers like NPM, Bower, or Yarn to get the packages that you need into the websites that you want.</div>

--------
