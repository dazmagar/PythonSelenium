<!-- PythonSelenium Docs -->

## PythonSelenium Case Plans 🗂️

🗂️ <b>PythonSelenium Case Plans</b> is Test Case Management Software that uses Markdown tables for displaying test plans directly in GitHub (and other source code management systems that support Markdown format).

🗂️ The ``case_summary.md`` file is generated from individual Case Plans that exist in the ``case_plans/`` folders of your repository. (See the example below to learn how the Case Summary file may look.)

--------

> **Example of a ``case_summary.md`` file:**

<h2>Summary of existing Case Plans</h2>

|   |    |   |
| - | -: | - |
| 🔵 | 8 | Case Plans with customized tables |
| ⭕ | 2 | Case Plans using boilerplate code |
| 🚧 | 1 | Case Plan that is missing a table |

--------

<h3>🔎 (Click rows to expand) 🔍</h3>

<details>
<summary> 🔵 <code><b>basic_test.py::MyTestClass::test_basics</b></code></summary>

| # | Step Description | Expected Result |
| - | ---------------- | --------------- |
| 1 | Log in to https://www.saucedemo.com with ``standard_user``. | Login was successful. |
| 2 | Click on the ``Backpack`` ``ADD TO CART`` button. | The button text changed to ``REMOVE``. |
| 3 | Click on the cart icon. | The ``Backpack`` is seen in the cart. |
| 4 | Remove the ``Backpack`` from the cart. | The ``Backpack`` is no longer in the cart. |
| 5 | Log out from the website. | Logout was successful. |

</details>

<details>
<summary> ⭕ <code><b>locale_code_test.py::LocaleCodeTests::test_locale_code</b></code></summary>

| # | Step Description | Expected Result |
| - | ---------------- | --------------- |
| 1 | Perform Action 1 | Verify Action 1 |
| 2 | Perform Action 2 | Verify Action 2 |

</details>

<details>
<summary> 🔵 <code><b>my_first_test.py::MyTestClass::test_swag_labs</b></code></summary>

| # | Step Description | Expected Result |
| - | ---------------- | --------------- |
| 1 | Log in to https://www.saucedemo.com with ``standard_user``. | Login was successful. |
| 2 | Click on the ``Backpack`` ``ADD TO CART`` button. | The button text changed to ``REMOVE``. |
| 3 | Click on the cart icon. | The ``Backpack`` is seen in the cart. |
| 4 | Click on the ``CHECKOUT`` button. <br /> Enter user details and click ``CONTINUE``. | The ``Backpack`` is seen in the cart on the ``CHECKOUT: OVERVIEW`` page. |
| 5 | Click on the ``FINISH`` button. | There is a ``Thank You`` message and a ``Pony Express`` delivery logo. |
| 6 | Log out from the website. | Logout was successful. |

</details>

<details>
<summary> ⭕ <code><b>proxy_test.py::ProxyTests::test_proxy</b></code></summary>

| # | Step Description | Expected Result |
| - | ---------------- | --------------- |
| 1 | Perform Action 1 | Verify Action 1 |
| 2 | Perform Action 2 | Verify Action 2 |

</details>

--------

🗂️ Before you can generate a ``case_summary.md`` file that includes your existing Case Plans, first you'll need to select which existing tests you want to create boilerplate Case Plans from. For that, you can use the PythonSelenium Case Plans GUI:

```bash
pysel caseplans
```

🗂️ Once you are running the Case Plans GUI, select the existing tests that need Case Plans, and then click: ``Generate boilerplate Case Plans for selected tests missing them``. For each selected test that didn't already have a Case Plan file, one will be generated. Each new Case Plan file starts with default boilerplate code with a Markdown table. Eg:

```bash
``proxy_test.py::ProxyTests::test_proxy``
---
| # | Step Description | Expected Result |
| - | ---------------- | --------------- |
| 1 | Perform Action 1 | Verify Action 1 |
| 2 | Perform Action 2 | Verify Action 2 |

```

🗂️ When rendered as a Markdown table, the result looks like this:

``proxy_test.py::ProxyTests::test_proxy``
---
| # | Step Description | Expected Result |
| - | ---------------- | --------------- |
| 1 | Perform Action 1 | Verify Action 1 |
| 2 | Perform Action 2 | Verify Action 2 |

🗂️ Markdown tables are flexible, but must be constructed correctly to be displayed. For a Markdown table to render, it's important that you place pipes (``|``), dashes (``-``), and spaces in the correct locations. If you want a line break in a step, use ``<br />``. If you want an empty step, put a space between pipes, eg: ``| |``.

🗂️ Here's an example of a Case Plan for [my_first_test.py](/examples/my_first_test.py):

``my_first_test.py::MyTestClass::test_swag_labs``
---
| # | Step Description | Expected Result |
| - | ---------------- | --------------- |
| 1 | Log in to https://www.saucedemo.com with ``standard_user``. | Login was successful. |
| 2 | Click on the ``Backpack`` ``ADD TO CART`` button. | The button text changed to ``REMOVE``. |
| 3 | Click on the cart icon. | The ``Backpack`` is seen in the cart. |
| 4 | Click on the ``CHECKOUT`` button. <br /> Enter user details and click ``CONTINUE``. | The ``Backpack`` is seen in the cart on the ``CHECKOUT: OVERVIEW`` page. |
| 5 | Click on the ``FINISH`` button. | There is a ``Thank you`` message. |
| 6 | Log out from the website. | Logout was successful. |

🗂️ After you've created some Case Plans, you can use the ``Generate Summary of existing Case Plans`` button in the Case Plans GUI to generate the Case Plans Summary file.

🗂️ The generated Case Plans summary file, ``case_summary.md``, gets created in the same location where the Case Plans GUI was launched. This is NOT the same location where individual Case Plan boilerplates are generated, which is in the ``case_plans/`` folders. The ``case_plans/`` folders are generated where individual tests live, which means that if you have your tests in multiple folders, then you could also have multiple ``case_plans/`` folders. A ``case_summary.md`` file may look like this when rendered:

🗂️ When calling ``pysel caseplans``, you can provide additional arguments to limit the tests that appear in the list. The same discovery rules apply as when using ``pytest``. Eg:

```bash
pysel caseplans
pysel caseplans -k agent
pysel caseplans -m marker2
pysel caseplans test_suite.py
pysel caseplans offline_examples/
```

--------
