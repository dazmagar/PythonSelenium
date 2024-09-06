<!-- PythonSelenium Docs -->

<h2>The Selenium Grid Hub:</h2>

The Selenium Grid Hub lets you distribute tests to run in parallel across multiple node machines. Each node machine can then run its own allocation of tests. This allows you to run a large suite of tests very quickly.

<h3>Running the Selenium Grid Hub:</h3>

The following commands will work once you've installed pythonselenium.

<h4>Downloading the Selenium Server JAR file:</h4>

```bash
pythonselenium download server
```

* (Required for using your own Selenium Grid)

<h4>Grid Hub server controls:</h4>

```bash
pythonselenium grid-hub {start|stop|restart} [OPTIONS]
```

<b>Options:</b>
<ul>
<li> -v / --verbose  (Increases verbosity of logging output.)</li>
<li> --timeout=TIMEOUT  (Close idle browser after TIMEOUT sec.)</li>
</ul>

<h4>Grid node server controls:</h4>

```bash
pythonselenium grid-node {start|stop|restart} --hub=[HUB_IP] [OPTIONS]
```

<b>Options:</b>
<ul>
<li> -v / --verbose  (Increases verbosity of logging output.)</li>
<li> --hub=[HUB_IP]  (Specifies the Grid Hub to connect to. Default: "127.0.0.1".)</li>
</ul>

When the Grid Hub Console is up and running, you'll be able to find it here: [http://127.0.0.1:4444/grid/console](http://127.0.0.1:4444/grid/console)

Now you can run your tests on the Selenium Grid:

```bash
pytest test_demo_site.py --server=IP_ADDRESS --port=4444
```

You can also run your tests on someone else's Selenium Grid to avoid managing your own. Here are some Selenium Grids that you can use (and the run command format):

* [BrowserStack](https://www.browserstack.com/automate#) Selenium Grid:

```bash
pytest test_demo_site.py --server=USERNAME:KEY@hub.browserstack.com --port=80
```

* [Sauce Labs](https://saucelabs.com/products/platform-configurator) Selenium Grid:

```bash
pytest test_demo_site.py --server=USERNAME:KEY@ondemand.us-east-1.saucelabs.com --port=443 --protocol=https
```

* [CrossBrowserTesting](https://help.crossbrowsertesting.com/selenium-testing/getting-started/python/) Selenium Grid:

```bash
pytest test_demo_site.py --server=USERNAME:KEY@hub.crossbrowsertesting.com --port=80
```

To use a server on the ``https`` protocol, add ``--protocol=https``:
(<i>PythonSelenium 1.65.2 and newer uses ``https`` automatically for ``--port=443``.</i>)

```bash
pytest test_demo_site.py --protocol=https --server=IP_ADDRESS --port=PORT
```

* (For setting browser desired capabilities while running Selenium remotely, see the [desired capabilities documentation](/help_docs/desired_capabilities.md))

<h4>More info about the Selenium Grid Hub can be found here:</h4>

* [https://www.selenium.dev/documentation/grid/](https://www.selenium.dev/documentation/grid/)
