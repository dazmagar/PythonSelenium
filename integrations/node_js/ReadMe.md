<h2>Creating a Test Runner with NodeJS + Express</h2>

You can create a customized web app for running PythonSelenium tests by using NodeJS and Express. (This tutorial assumes that you've already installed [PythonSelenium](/).

#### 0. Clone PythonSelenium from GitHub

* You'll need to work with the files located in the [integrations/node_js](/integrations/node_js) folder.

#### 1. Install NodeJS (if not installed)

* Navigate to [https://nodejs.org/en/](https://nodejs.org/en/)
* Click to download and install NodeJS

#### 2. Upgrade NodeJS (if using an older version)

```bash
npm install -g npm@latest
```

#### 3. Install the Example Test Runner for PythonSelenium from the [integrations/node_js](/integrations/node_js) folder (``npm ci`` has a speed improvement over ``npm install`` because it uses the ``npm-shrinkwrap.json`` file that's generated via ``npm shrinkwrap``.)

```bash
npm ci
```

(You should see a ``node_modules`` folder appear in your ``node_js`` folder.)

#### 4. Run the NodeJS server for your PythonSelenium Test Runner web app

```bash
node server.js
```

(You can stop the server by using <kbd>Ctrl+C</kbd>)

#### 5. Open the PythonSelenium Test Runner web app

* Navigate to [http://127.0.0.1:3000/](http://127.0.0.1:3000/)

#### 6. Run an example test

Click on a button to run a PythonSelenium example test.

#### 7. Expand your web app

Now that you have a web app for running PythonSelenium tests, you can expand it to run any script that you want after pressing a button.
