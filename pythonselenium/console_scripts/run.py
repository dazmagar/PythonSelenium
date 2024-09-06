"""
PythonSelenium console scripts runner

Usage:
pythonselenium [COMMAND] [PARAMETERS]
  OR     pysel [COMMAND] [PARAMETERS]

Examples:
pysel get chromedriver
pysel methods
pysel options
pysel commander
pysel behave-gui
pysel behave-options
pysel caseplans
pysel mkdir ui_tests
pysel mkfile new_test.py
pysel mkrec new_test.py
pysel mkrec new_test.py --url=wikipedia.org
pysel codegen new_test.py --url=wikipedia.org
pysel recorder
pysel record new_test.py
pysel record
pysel mkchart new_chart.py
pysel convert webdriver_unittest_file.py
pysel print my_first_test.py -n
pysel extract-objects my_first_test.py
pysel inject-objects my_first_test.py
pysel objectify my_first_test.py
pysel revert-objects my_first_test.py
pysel encrypt
pysel decrypt
pysel proxy
pysel proxy --hostname=127.0.0.1 --port=8899
pysel download server
pysel grid-hub start
pysel grid-node start --hub=127.0.0.1
"""
import sys
import time

import colorama

from pythonselenium.config import settings
from pythonselenium.fixtures import constants, shared_utils

if shared_utils.is_windows() and hasattr(colorama, "just_fix_windows_console"):
    colorama.just_fix_windows_console()
else:
    colorama.init(autoreset=True)


def show_usage():
    show_basic_usage()
    sc = ""
    sc += '    Type "pysel help [COMMAND]" for specific command info.\n'
    sc += '    For info on all commands, type: "pythonselenium --help".\n'
    sc += '    Use "pytest" for running tests.\n'
    if "linux" not in sys.platform:
        c1 = colorama.Fore.BLUE + colorama.Back.LIGHTCYAN_EX
        c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
        c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
        c4 = colorama.Fore.MAGENTA + colorama.Back.LIGHTYELLOW_EX
        cr = colorama.Style.RESET_ALL
        sc = sc.replace("pythonselenium", c1 + "python" + c2 + "selenium" + cr)
        sc = sc.replace("pysel", c1 + "py" + c2 + "sel" + cr)
        sc = sc.replace("pytest", c3 + "pytest" + cr)
        sc = sc.replace("--help", c4 + "--help" + cr)
        sc = sc.replace("help", c4 + "help" + cr)
    print(sc)


def show_basic_usage():
    from pythonselenium.console_scripts import logo_helper

    pythonselenium_logo = logo_helper.get_pythonselenium_logo()
    print(pythonselenium_logo)
    print("")
    time.sleep(0.28)  # Enough time to see the logo
    show_package_location()
    show_version_info()
    print("")
    time.sleep(0.62)  # Enough time to see the version
    sc = ""
    sc += ' * USAGE: "pythonselenium [COMMAND] [PARAMETERS]"\n'
    sc += ' *    OR:          "pysel [COMMAND] [PARAMETERS]"\n'
    sc += "\n"
    sc += "COMMANDS:\n"
    sc += "      get / install    [DRIVER] [OPTIONS]\n"
    sc += "      methods          (List common Python methods)\n"
    sc += "      options          (List common pytest options)\n"
    sc += "      behave-options   (List common behave options)\n"
    sc += "      gui / commander  [OPTIONAL PATH or TEST FILE]\n"
    sc += "      behave-gui       (pysel Commander for Behave)\n"
    sc += "      caseplans        [OPTIONAL PATH or TEST FILE]\n"
    sc += "      mkdir            [DIRECTORY] [OPTIONS]\n"
    sc += "      mkfile           [FILE.py] [OPTIONS]\n"
    sc += "      mkrec / codegen  [FILE.py] [OPTIONS]\n"
    sc += "      recorder         (Open Recorder Desktop App.)\n"
    sc += "      record           (If args: mkrec. Else: App.)\n"
    sc += "      mkchart          [FILE.py] [LANG]\n"
    sc += "      print            [FILE] [OPTIONS]\n"
    sc += "      convert          [WEBDRIVER_UNITTEST_FILE.py]\n"
    sc += "      extract-objects  [PS_FILE.py]\n"
    sc += "      inject-objects   [PS_FILE.py] [OPTIONS]\n"
    sc += "      objectify        [PS_FILE.py] [OPTIONS]\n"
    sc += "      revert-objects   [PS_FILE.py] [OPTIONS]\n"
    sc += "      encrypt / obfuscate\n"
    sc += "      decrypt / unobfuscate\n"
    sc += "      proxy            (Start a basic proxy server)\n"
    sc += "      download server  (Get Selenium Grid JAR file)\n"
    sc += "      grid-hub         [start|stop] [OPTIONS]\n"
    sc += "      grid-node        [start|stop] --hub=[HOST/IP]\n"
    sc += ' * (EXAMPLE: "pysel get chromedriver") *\n'
    sc += ""
    if "linux" not in sys.platform:
        c1 = colorama.Fore.BLUE + colorama.Back.LIGHTCYAN_EX
        c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
        cr = colorama.Style.RESET_ALL
        sc = sc.replace("pythonselenium", c1 + "python" + c2 + "selenium" + cr)
        sc = sc.replace("pysel", c1 + "py" + c2 + "sel" + cr)
    print(sc)


def show_install_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "get / install" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium install [DRIVER_NAME] [OPTIONS]")
    print("           OR: pythonselenium get [DRIVER_NAME] [OPTIONS]")
    print("           OR:      pysel install [DRIVER_NAME] [OPTIONS]")
    print("           OR:          pysel get [DRIVER_NAME] [OPTIONS]")
    print("  Drivers: chromedriver, geckodriver, edgedriver, iedriver, uc_driver")
    print("  Options:")
    print("           VERSION         Specify the version to download.")
    print("                           Tries to detect the needed version.")
    print("                           If using chromedriver or edgedriver,")
    print("                           you can use the major version integer.")
    print()
    print("           -p OR --path    Also copy the driver to /usr/local/bin")
    print("  Examples:")
    print("           pysel get chromedriver")
    print("           pysel get geckodriver")
    print("           pysel get edgedriver")
    print("           pysel get chromedriver 114")
    print("           pysel get chromedriver 114.0.5735.90")
    print("           pysel get chromedriver stable")
    print("           pysel get chromedriver beta")
    print("           pysel get chromedriver -p")
    print("  Output:")
    print("           Downloads the webdriver to pythonselenium/drivers/")
    print("           (chromedriver is required for Chrome automation)")
    print("           (geckodriver is required for Firefox automation)")
    print("           (edgedriver is required for MS__Edge automation)")
    print("")


def show_commander_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "commander" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium commander [OPTIONAL PATH or TEST FILE]")
    print("           OR:      pysel commander [OPTIONAL PATH or TEST FILE]")
    print("           OR:   pythonselenium gui [OPTIONAL PATH or TEST FILE]")
    print("           OR:            pysel gui [OPTIONAL PATH or TEST FILE]")
    print("  Examples:")
    print("           pysel gui")
    print("           pysel gui -k agent")
    print("           pysel gui -m marker2")
    print("           pysel gui test_suite.py")
    print("           pysel gui offline_examples/")
    print("  Output:")
    print("           Launches PythonSelenium Commander | GUI for pytest.")
    print("")


def show_behave_gui_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "behave-gui" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium behave-gui [OPTIONAL PATH or TEST FILE]")
    print("           pythonselenium gui-behave [OPTIONAL PATH or TEST FILE]")
    print("           OR:    pysel behave-gui [OPTIONAL PATH or TEST FILE]")
    print("           OR:    pysel gui-behave [OPTIONAL PATH or TEST FILE]")
    print("  Examples:")
    print("           pysel behave-gui")
    print("           pysel behave-gui features/")
    print("           pysel behave-gui features/calculator.feature")
    print("  Output:")
    print("           Launches PythonSelenium Commander | GUI for Behave.")
    print("")


def show_caseplans_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "caseplans" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium caseplans [OPTIONAL PATH or TEST FILE]")
    print("           OR:      pysel caseplans [OPTIONAL PATH or TEST FILE]")
    print("  Examples:")
    print("           pysel caseplans")
    print("           pysel caseplans -k agent")
    print("           pysel caseplans -m marker2")
    print("           pysel caseplans test_suite.py")
    print("           pysel caseplans offline_examples/")
    print("  Output:")
    print("           Launches the PythonSelenium Case Plans Generator.")
    print("")


def show_mkdir_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "mkdir" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium mkdir [DIRECTORY] [OPTIONS]")
    print("           OR:      pysel mkdir [DIRECTORY] [OPTIONS]")
    print("  Example:")
    print("           pysel mkdir ui_tests")
    print("  Options:")
    print("           -b / --basic  (Only config files. No tests added.)")
    print("  Output:")
    print("           Creates a new folder for running PySel scripts.")
    print("           The new folder contains default config files,")
    print("           sample tests for helping new users get started,")
    print("           and Python boilerplates for setting up customized")
    print("           test frameworks.")
    print("")


def show_mkfile_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "mkfile" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium mkfile [FILE.py] [OPTIONS]")
    print("           OR:      pysel mkfile [FILE.py] [OPTIONS]")
    print("  Example:")
    print("           pysel mkfile new_test.py")
    print("  Options:")
    print("           -b / --basic  (Basic boilerplate / single-line test)")
    print("           -r / --rec  (adds Pdb+ breakpoint for Recorder Mode)")
    print("           --url=URL  (makes the test start on a specific page)")
    print("  Language Options:")
    print("           --en / --English ")
    print("  Syntax Formats:")
    print("           --bc / --basecase       (BaseCase class inheritance)")
    print("           --pf / --pytest-fixture          (ps pytest fixture)")
    print("           --cf / --class-fixture   (class + ps pytest fixture)")
    print("           --cm / --context-manager        (ps context manager)")
    print("           --dc / --driver-context      (DriverContext manager)")
    print("           --dm / --driver-manager             (Driver manager)")
    print("  Output:")
    print("           Creates a new PySel test file with boilerplate code.")
    print("           If the file already exists, an error is raised.")
    print("           By default, uses English with BaseCase inheritance,")
    print("           and creates a boilerplate with common PythonSelenium")
    print('           methods: "open", "type", "click", "assert_element",')
    print('           and "assert_text". If using the basic boilerplate')
    print('           option, only the "open" method is included. Only the')
    print("           BaseCase format supports Languages or Recorder Mode.")
    print("")


def show_mkrec_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "mkrec" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium mkrec [FILE.py] [OPTIONS]")
    print("           OR:      pysel mkrec [FILE.py] [OPTIONS]")
    print("  Examples:")
    print("           pysel mkrec new_test.py")
    print("           pysel mkrec new_test.py --url=wikipedia.org")
    print("  Options:")
    print("           --url=URL  (Sets the initial start page URL.)")
    print("           --edge  (Use Edge browser instead of Chrome.)")
    print("           --gui / --headed  (Use headed mode on Linux.)")
    print("           --uc / --undetected  (Use undetectable mode.)")
    print("           --ee  (Use SHIFT + ESC to end the recording.)")
    print("           --overwrite  (Overwrite file when it exists.)")
    print("           --behave  (Also output Behave/Gherkin files.)")
    print("  Output:")
    print("           Creates a new pythonselenium test using the Recorder.")
    print("           If the filename already exists, an error is raised.")
    print("")


def show_codegen_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "codegen" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium codegen [FILE.py] [OPTIONS]")
    print("           OR:      pysel codegen [FILE.py] [OPTIONS]")
    print("  Examples:")
    print("           pysel codegen new_test.py")
    print("           pysel codegen new_test.py --url=wikipedia.org")
    print("  Options:")
    print("           --url=URL  (Sets the initial start page URL.)")
    print("           --edge  (Use Edge browser instead of Chrome.)")
    print("           --gui / --headed  (Use headed mode on Linux.)")
    print("           --uc / --undetected  (Use undetectable mode.)")
    print("           --ee  (Use SHIFT + ESC to end the recording.)")
    print("           --overwrite  (Overwrite file when it exists.)")
    print("           --behave  (Also output Behave/Gherkin files.)")
    print("  Output:")
    print("           Creates a new pythonselenium test using the Recorder.")
    print("           If the filename already exists, an error is raised.")
    print("")


def show_recorder_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "recorder" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium recorder [OPTIONS]")
    print("           OR:      pysel recorder [OPTIONS]")
    print("  Options:")
    print("           --uc / --undetected  (Use undetectable mode.)")
    print("           --behave  (Also output Behave/Gherkin files.)")
    print("  Output:")
    print("           Launches the pythonselenium Recorder Desktop App.")
    print("")


def show_mkchart_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "mkchart" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium mkchart [FILE.py] [LANG]")
    print("           OR:      pysel mkchart [FILE.py] [LANG]")
    print("  Example:")
    print("           pysel mkchart new_chart.py --en")
    print("  Language Options:")
    print("           --en / --English ")
    print("  Output:")
    print("           Creates a new PythonSelenium chart presentation.")
    print("           If the file already exists, an error is raised.")
    print("           By default, the slides are written in English,")
    print('           and use a "sky" theme with "slide" transition.')
    print("           The chart can be used as a basic boilerplate.")
    print("")


def show_convert_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "convert" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium convert [WEBDRIVER_UNITTEST_FILE.py]")
    print("           OR:      pysel convert [WEBDRIVER_UNITTEST_FILE.py]")
    print("  Output:")
    print("           Converts a Selenium IDE exported WebDriver unittest")
    print("           file into a PythonSelenium file. Adds _PS to the new")
    print("           file name while keeping the original file intact.")
    print("           (Works with Katalon Recorder Selenium scripts.)")
    print("")


def show_print_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "print" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium print [FILE] [OPTIONS]")
    print("           OR:      pysel print [FILE] [OPTIONS]")
    print("  Options:")
    print("           -n   (Add line Numbers to the rows)")
    print("  Output:")
    print("           Prints the code/text of any file")
    print("           with syntax-highlighting.")
    print("")

def show_extract_objects_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "extract-objects" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium extract-objects [PS_FILE.py]")
    print("           OR:      pysel extract-objects [PS_FILE.py]")
    print("  Output:")
    print("           Creates page objects based on selectors found in a")
    print("           PythonSelenium Python file and saves those objects to the")
    print('           "page_objects.py" file in the same folder as the tests.')
    print("")


def show_inject_objects_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "inject-objects" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium inject-objects [PS_FILE.py] [OPTIONS]")
    print("           OR:      pysel inject-objects [PS_FILE.py] [OPTIONS]")
    print("  Options:")
    print("           -c, --comments  (Add object selectors to the comments.)")
    print("                           (Default: No added comments.)")
    print("  Output:")
    print('           Takes the page objects found in the "page_objects.py"')
    print("           file and uses those to replace matching selectors in")
    print("           the selected PythonSelenium Python file.")
    print("")


def show_objectify_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "objectify" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium objectify [PS_FILE.py] [OPTIONS]")
    print("           OR:      pysel objectify [PS_FILE.py] [OPTIONS]")
    print("  Options:")
    print("           -c, --comments  (Add object selectors to the comments.)")
    print("                           (Default: No added comments.)")
    print("  Output:")
    print("           A modified version of the file where the selectors")
    print("           have been replaced with variable names defined in")
    print('           "page_objects.py", supporting the Page Object Pattern.')
    print("")
    print('           (pythonselenium "objectify" has the same outcome as')
    print('            combining "extract-objects" with "inject-objects")')
    print("")


def show_revert_objects_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "revert-objects" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium revert-objects [PS_FILE.py] [OPTIONS]")
    print("           OR:      pysel revert-objects [PS_FILE.py] [OPTIONS]")
    print("  Options:")
    print("           -c, --comments  (Keep existing comments for the lines.)")
    print("                           (Default: No comments are kept.)")
    print("  Output:")
    print('           Reverts the changes made by "pythonselenium objectify" or')
    print('           "pythonselenium inject-objects" when run against a')
    print("           PythonSelenium file. Objects will get replaced by")
    print('           selectors stored in the "page_objects.py" file.')
    print("")


def show_encrypt_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "encrypt OR obfuscate" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium encrypt   ||   pythonselenium obfuscate")
    print("                                  --OR--")
    print("                    pysel encrypt   ||            pysel obfuscate")
    print("  Output:")
    print("           Runs the password encryption/obfuscation tool.")
    print("           (Where you can enter a password to encrypt/obfuscate.)")
    print("")


def show_decrypt_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "decrypt OR unobfuscate" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium decrypt   ||   pythonselenium unobfuscate")
    print("                                  --OR--")
    print("                    pysel decrypt   ||            pysel unobfuscate")
    print("  Output:")
    print("           Runs the password decryption/unobfuscation tool.")
    print("           (Where you can enter an encrypted password to decrypt.)")
    print("")


def show_download_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "download" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium download server")
    print("           OR:      pysel download server")
    print("  Output:")
    print("           Downloads the Selenium Standalone Server.")
    print("           (Server is required for using your own Selenium Grid.)")
    print("")


def show_grid_hub_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "grid-hub" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium grid-hub {start|stop|restart} [OPTIONS]")
    print("           OR:      pysel grid-hub {start|stop|restart} [OPTIONS]")
    print("  Options:")
    print("           -v, --verbose  (Increase verbosity of logging output.)")
    print("                          (Default: Quiet logging / not verbose.)")
    print("           --timeout=TIMEOUT  (Close idle browser after TIMEOUT.)")
    print("                              (The default TIMEOUT: 230 seconds.)")
    print("                              (Use --timeout=0 to skip timeouts.)")
    print("  Example:")
    print("           pythonselenium grid-hub start")
    print("  Output:")
    print("           Controls the Selenium Grid Hub Server, which allows")
    print("           for running tests on multiple machines in parallel")
    print("           to speed up test runs and reduce the total time")
    print("           of test suite execution.")
    print('           You can "start" or "stop" the Grid Hub server.')
    print("")


def show_grid_node_usage():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "  " + c2 + "** " + c3 + "grid-node" + c2 + " **" + cr
    print(sc)
    print("")
    print("  Usage:")
    print("           pythonselenium grid-node {start|stop|restart} [OPTIONS]")
    print("           OR:      pysel grid-node {start|stop|restart} [OPTIONS]")
    print("  Options:")
    print("           --hub=[HOST/IP]  (The Grid Hub Hostname / IP Address.)")
    print("                                 (Default: 127.0.0.1 if not set.)")
    print("           -v, --verbose  (Increase verbosity of logging output.)")
    print("                          (Default: Quiet logging / Not verbose.)")
    print("  Example:")
    print("           pythonselenium grid-node start --hub=127.0.0.1")
    print("  Output:")
    print("           Controls the Selenium Grid node, which serves as a")
    print("           worker machine for your Selenium Grid Hub server.")
    print('           You can "start" or "stop" the Grid node.')
    print("")


def get_version_info():
    from pythonselenium import __version__

    version_info = None
    c1 = colorama.Fore.BLUE + colorama.Back.LIGHTCYAN_EX
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    ps_text = c1 + "selenium" + c2 + "base" + cr
    version_info = "%s %s%s%s" % (ps_text, c3, __version__, cr)
    return version_info


def show_version_info():
    version_info = get_version_info()
    print("%s" % version_info)


def get_package_location():
    import os

    import pythonselenium

    location = os.path.dirname(os.path.realpath(pythonselenium.__file__))
    if location.endswith("pythonselenium"):
        location = location[0 : -len("pythonselenium")]  # noqa: E203
    return location


def show_package_location():
    location = get_package_location()
    print("%s" % location)


def show_methods():
    c1 = colorama.Fore.BLUE + colorama.Back.LIGHTCYAN_EX
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    c4 = colorama.Fore.MAGENTA + colorama.Back.LIGHTYELLOW_EX
    c5 = colorama.Fore.LIGHTRED_EX + colorama.Back.LIGHTGREEN_EX
    cr = colorama.Style.RESET_ALL
    sc = (
        "\n " + c2 + " ** " + c3 + " PythonSelenium Methods "
        "" + c2 + " ** " + cr
    )
    print(sc)
    print("")
    line = "Here are some common methods that come with PythonSelenium:"
    line = c1 + line + cr
    print(line)
    line = "(Some optional args are not shown here)"
    print(line)
    print("")
    psm = ""
    psm += "*.open(url) => Navigate the browser window to the URL.\n"
    psm += "*.type(selector, text) => Update the field with the text.\n"
    psm += "*.click(selector) => Click the element with the selector.\n"
    psm += "*.click_link(link_text) => Click the link containing text.\n"
    psm += "*.check_if_unchecked(selector) => Check checkbox if unchecked.\n"
    psm += "*.uncheck_if_checked(selector) => Uncheck checkbox if checked.\n"
    psm += "*.select_option_by_text(dropdown_selector, option)\n"
    psm += "*.hover_and_click(hover_selector, click_selector)\n"
    psm += "*.drag_and_drop(drag_selector, drop_selector)\n"
    psm += "*.choose_file(selector, file_path) => Choose a file to upload.\n"
    psm += "*.get_text(selector) => Get the text from the element.\n"
    psm += "*.get_current_url() => Get the URL of the current page.\n"
    psm += "*.get_page_source() => Get the HTML of the current page.\n"
    psm += "*.get_attribute(selector, attribute) => Get element attribute.\n"
    psm += "*.get_title() => Get the title of the current page.\n"
    psm += "*.go_back() => Navigate to the previous page in history.\n"
    psm += "*.switch_to_frame(frame) => Switch into the iframe container.\n"
    psm += "*.switch_to_default_content() => Exit all iframe containers.\n"
    psm += "*.switch_to_parent_frame() => Exit from the current iframe.\n"
    psm += "*.open_new_window() => Open a new window in the same browser.\n"
    psm += "*.switch_to_window(window) => Switch to the browser window.\n"
    psm += "*.switch_to_default_window() => Switch to the original window.\n"
    psm += "*.get_new_driver(OPTIONS) => Open a new driver with OPTIONS.\n"
    psm += "*.switch_to_driver(driver) => Switch to the browser driver.\n"
    psm += "*.switch_to_default_driver() => Switch to the original driver.\n"
    psm += "*.wait_for_element(selector) => Wait until element is visible.\n"
    psm += "*.wait_for_element_present(selector) => Until element in HTML.\n"
    psm += "*.is_element_visible(selector) => Return element visibility.\n"
    psm += "*.is_element_present(selector) => Return element is in HTML.\n"
    psm += "*.is_text_visible(text, selector) => Return text visibility.\n"
    psm += "*.is_checked(selector) => Return whether the box is checked.\n"
    psm += "*.sleep(seconds) => Do nothing for the given amount of time.\n"
    psm += "*.save_screenshot(name) => Save a screenshot in .png format.\n"
    psm += "*.assert_element(selector) => Verify the element is visible.\n"
    psm += "*.assert_text(text, selector) => Verify text in the element.\n"
    psm += "*.assert_exact_text(text, selector) => Verify text is exact.\n"
    psm += "*.assert_url(url) => Verify that the current URL is the URL.\n"
    psm += "*.assert_url_contains(substring) => Verify substring in URL.\n"
    psm += "*.assert_title(title) => Verify the title of the web page.\n"
    psm += "*.assert_title_contains(substring) => Verify STR in title.\n"
    psm += "*.assert_downloaded_file(file) => Verify file was downloaded.\n"
    psm += "*.assert_no_404_errors() => Verify there are no broken links.\n"
    psm += "*.assert_no_js_errors() => Verify there are no JS errors.\n"
    psm = psm.replace("*.", "self." + c1).replace("(", cr + "(")
    psm = psm.replace("self.", c2 + "self" + c5 + "." + cr)
    psm = psm.replace("(", c3 + "(" + c4)
    psm = psm.replace(")", c3 + ")" + cr)
    print(psm)


def show_options():
    c1 = colorama.Fore.BLUE + colorama.Back.LIGHTCYAN_EX
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    c4 = colorama.Fore.MAGENTA + colorama.Back.LIGHTYELLOW_EX
    c5 = colorama.Fore.RED + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "\n " + c2 + " ** " + c3 + " pytest CLI Options " + c2 + " ** " + cr
    print(sc)
    print("")
    line = "Here are some common pytest options to use with PythonSelenium:"
    line = c1 + line + cr
    print(line)
    line = '(Some options are Chromium-specific, e.g. "--guest --mobile")'
    print(line)
    op = "\n"
    op += '--browser=BROWSER  (Choice of web browser. Default is "chrome".)\n'
    op += "--edge / --firefox / --safari  (Shortcut for browser selection.)\n"
    op += "--headless  (Run tests headlessly. Default setting on Linux OS.)\n"
    op += "--demo  (Slow down and visually see test actions as they occur.)\n"
    op += "--slow  (Slow down the automation. Faster than using Demo Mode.)\n"
    op += "--rs / --reuse-session  (Reuse browser session between tests.)\n"
    op += "--reuse-class-session / --rcs  (RS, but for class tests only.)\n"
    op += "--crumbs  (Clear all cookies between tests reusing a session.)\n"
    op += "--maximize  (Start tests with the web browser window maximized.)\n"
    op += "--dashboard  (Enable PythonSelenium's Dashboard at dashboard.html)\n"
    op += "--incognito  (Enable Chromium's Incognito Mode.)\n"
    op += "--guest  (Enable Chromium's Guest Mode.)\n"
    op += "--dark  (Enable Chromium's Dark Mode.)\n"
    op += "--uc  (Use undetected-chromedriver to evade detection.)\n"
    op += "-m=MARKER  (Run tests with the specified pytest marker.)\n"
    op += "-n=NUM  (Multithread the tests using that many threads.)\n"
    op += "-v  (Verbose mode. Print the full names of each test run.)\n"
    op += "--html=report.html  (Create a detailed pytest-html report.)\n"
    op += "--collect-only / --co  (Only show discovered tests. No run.)\n"
    op += "--co -q  (Only show full names of discovered tests. No run.)\n"
    op += "-x  (Stop running tests after the first failure is reached.)\n"
    op += "--pdb  (Enter the Post Mortem Debug Mode after any test fails.)\n"
    op += "--trace  (Enter Debug Mode immediately after starting any test.)\n"
    op += "      | Debug Mode Commands  >>>   help / h: List all commands. |\n"
    op += "      |   n: Next line of method. s: Step through. c: Continue. |\n"
    op += "      |  return / r: Run until method returns. j: Jump to line. |\n"
    op += "      | where / w: Show stack spot. u: Up stack. d: Down stack. |\n"
    op += "      | longlist / ll: See code. dir(): List namespace objects. |\n"
    op += "--help / -h  (Display list of all available pytest options.)\n"
    op += "--ftrace / --final-trace  (Enter Debug Mode after any test.)\n"
    op += "--recorder / --rec  (Save browser actions as Python scripts.)\n"
    op += "--rec-behave / --rec-gherkin  (Save actions as Gherkin code.)\n"
    op += "--rec-print  (Display recorded scripts when they are created.)\n"
    op += "--save-screenshot  (Save a screenshot at the end of each test.)\n"
    op += "--archive-logs  (Archive logs after tests to prevent deletion.)\n"
    op += "--check-js  (Check for JavaScript errors after page loads.)\n"
    op += "--start-page=URL  (The browser start page when tests begin.)\n"
    op += "--agent=STRING  (Modify the web browser's User-Agent string.)\n"
    op += "--mobile  (Use Chromium's mobile device emulator during tests.)\n"
    op += '--metrics=STRING  (Set mobile "CSSWidth,CSSHeight,PixelRatio".)\n'
    op += "--ad-block  (Block certain types of iframe ads from appearing.)\n"
    op += "--settings-file=FILE  (Override default PythonSelenium settings.)\n"
    op += '--env=ENV  (Set the test env. Access with "self.env" in tests.)\n'
    op += '--data=DATA  (Extra test data. Access with "self.data" in tests.)\n'
    op += "--disable-csp  (Disable the Content Security Policy of websites.)\n"
    op += "--remote-debug  (Sync to Ch-R-Debugger chrome://inspect/#devices)\n"
    op += "--server=SERVER  (The Selenium Grid server/IP used for tests.)\n"
    op += "--port=PORT  (The Selenium Grid port used by the test server.)\n"
    op += "--proxy=SERVER:PORT  (Connect to a proxy server:port for tests.)\n"
    op += "--proxy=USER:PASS@SERVER:PORT  (Use authenticated proxy server.)\n"
    op += cr
    op = op.replace("\n-", "\n" + c1 + "-").replace("  (", cr + "  (")
    op = op.replace(" / -", cr + " / " + c1 + "-")
    op = op.replace("=", c2 + "=" + c3)
    op = op.replace(" | ", " |" + c3 + " ").replace("|\n", cr + "|\n")
    op = op.replace(": ", c5 + ":" + c3 + " ")
    op = op.replace("Debug Mode Commands", c5 + "Debug Mode Commands" + c3)
    op = op.replace(">>>", c4 + ">>>" + c3)
    print(op)
    line = "For the full list of " + c2 + "command-line options" + cr
    line += ', type: "' + c3 + "pytest" + cr + " " + c1 + "--help" + cr + '".'
    print(line)
    print("")


def show_behave_options():
    c1 = colorama.Fore.BLUE + colorama.Back.LIGHTCYAN_EX
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    c4 = colorama.Fore.MAGENTA + colorama.Back.LIGHTYELLOW_EX
    c5 = colorama.Fore.RED + colorama.Back.LIGHTYELLOW_EX
    cr = colorama.Style.RESET_ALL
    sc = "\n " + c2 + " ** " + c3 + " Behave CLI Options " + c2 + " ** " + cr
    print(sc)
    print("")
    line = 'Here are some common "behave" options to use with PythonSelenium:'
    line = c1 + line + cr
    print(line)
    line = '(Some options are Chromium-specific, e.g. "-D guest -D mobile")'
    print(line)
    op = "\n"
    op += '-D browser=BROWSER  (The web browser to use. Default is "chrome")\n'
    op += "-D headless  (Run tests headlessly. Default mode on Linux OS.)\n"
    op += "-D demo  (Slow down and visually see test actions as they occur.)\n"
    op += "-D slow  (Slow down the automation. Faster than using Demo Mode.)\n"
    op += "-D reuse-session / -D rs  (Reuse browser session between tests.)\n"
    op += "-D crumbs  (Clear all cookies between tests reusing a session.)\n"
    op += "-D maximize  (Start tests with the web browser window maximized.)\n"
    op += "-D dashboard  (Enable PythonSelenium's Dashboard at dashboard.html)\n"
    op += "-D incognito  (Enable Chromium's Incognito Mode.)\n"
    op += "-D guest  (Enable Chromium's Guest Mode.)\n"
    op += "-D dark  (Enable Chromium's Dark Mode.)\n"
    op += "-D uc  (Use undetected-chromedriver to evade detection.)\n"
    op += "--no-snippets / -q  (Quiet mode. Don't print snippets.)\n"
    op += "--dry-run / -d  (Dry run. Only show discovered tests.)\n"
    op += "--stop  (Stop running tests after the first failure is reached.)\n"
    op += "-D pdb  (Enter the Post Mortem Debug Mode after any test fails.)\n"
    op += "      | Debug Mode Commands  >>>   help / h: List all commands. |\n"
    op += "      |   n: Next line of method. s: Step through. c: Continue. |\n"
    op += "      |  return / r: Run until method returns. j: Jump to line. |\n"
    op += "      | where / w: Show stack spot. u: Up stack. d: Down stack. |\n"
    op += "      | longlist / ll: See code. dir(): List namespace objects. |\n"
    op += "-D recorder  (Record browser actions to generate test scripts.)\n"
    op += "-D rec-print  (Display recorded scripts when they are created.)\n"
    op += "-D save-screenshot  (Save a screenshot at the end of each test.)\n"
    op += "-D archive-logs  (Archive log files instead of deleting them.)\n"
    op += "-D check-js  (Check for JavaScript errors after page loads.)\n"
    op += "-D start-page=URL  (The browser start page when tests begin.)\n"
    op += "-D agent=STRING  (Modify the web browser's User-Agent string.)\n"
    op += "-D mobile  (Use Chromium's mobile device emulator during tests.)\n"
    op += '-D metrics=STRING  (Set mobile "CSSWidth,CSSHeight,PixelRatio".)\n'
    op += "-D ad-block  (Block some types of display ads after page loads.)\n"
    op += "-D settings-file=FILE  (Override default PythonSelenium settings.)\n"
    op += '-D env=ENV  (Set the test env. Access using "self.env" in tests.)\n'
    op += '-D data=DATA  (Extra test data. Access using "self.data".)\n'
    op += "-D disable-csp  (Disable the Content Security Policy of sites.)\n"
    op += "-D remote-debug  (Sync Ch-R-Debugger chrome://inspect/#devices)\n"
    op += "-D server=SERVER  (The Selenium Grid server/IP used for tests.)\n"
    op += "-D port=PORT  (The Selenium Grid port used by the test server.)\n"
    op += "-D proxy=SERVER:PORT  (Connect to a proxy server:port for tests.)\n"
    op += "-D proxy=USER:PASS@SERVER:PORT  (Use authenticated proxy server.)\n"
    op += cr
    op = op.replace("\n-", "\n" + c1 + "-").replace("  (", cr + "  (")
    op = op.replace(" / -", cr + " / " + c1 + "-")
    op = op.replace("=", c2 + "=" + c3)
    op = op.replace(" | ", " |" + c3 + " ").replace("|\n", cr + "|\n")
    op = op.replace(": ", c5 + ":" + c3 + " ")
    op = op.replace("Debug Mode Commands", c5 + "Debug Mode Commands" + c3)
    op = op.replace(">>>", c4 + ">>>" + c3)
    print(op)
    line = "For the full list of " + c2 + "command-line options" + cr
    line += ', type: "' + c3 + "behave" + cr + " " + c1 + "--help" + cr + '".'
    print(line)
    print("")


def show_detailed_help():
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    c3 = colorama.Fore.BLUE + colorama.Back.LIGHTYELLOW_EX
    c6 = colorama.Back.CYAN
    cr = colorama.Style.RESET_ALL
    show_basic_usage()
    print(c6 + "            " + c2 + "  Commands:  " + c6 + "            ")
    print(cr)
    show_install_usage()
    show_commander_usage()
    show_behave_gui_usage()
    show_caseplans_usage()
    show_mkdir_usage()
    show_mkfile_usage()
    show_mkrec_usage()
    show_codegen_usage()
    show_recorder_usage()
    show_mkchart_usage()
    show_convert_usage()
    show_print_usage()
    show_extract_objects_usage()
    show_inject_objects_usage()
    show_objectify_usage()
    show_revert_objects_usage()
    show_encrypt_usage()
    show_decrypt_usage()
    show_download_usage()
    show_grid_hub_usage()
    show_grid_node_usage()
    print('* (Use "' + c3 + "pytest" + cr + '" for running tests) *\n')


def main():
    command = None
    command_args = None
    num_args = len(sys.argv)
    if num_args == 1:
        show_usage()
        return
    elif num_args == 2:
        command = sys.argv[1]
        command_args = []
    elif num_args > 2:
        command = sys.argv[1]
        command_args = sys.argv[2:]
    command = command.lower()

    if command == "get" or command == "install":
        if len(command_args) >= 1:
            from pythonselenium.console_scripts import ps_install

            need_retry = False
            need_another_retry = False
            retry_msg_1 = "* Unable to download driver! Retrying in 3s..."
            retry_msg_2 = "** Unable to download driver! Retrying in 5s..."
            if " --proxy=" in " ".join(sys.argv):
                from pythonselenium.core import proxy_helper

                for arg in sys.argv:
                    if arg.startswith("--proxy="):
                        proxy_string = arg.split("--proxy=")[1]
                        if "@" in proxy_string:
                            proxy_string = proxy_string.split("@")[1]
                        proxy_helper.validate_proxy_string(proxy_string)
                        break
            try:
                settings.HIDE_DRIVER_DOWNLOADS = False
                ps_install.main()
            except Exception as e:
                invalid_run_cmd = constants.Warnings.INVALID_RUN_COMMAND
                if invalid_run_cmd in str(e):
                    raise
                print()
                print(retry_msg_1)
                time.sleep(3)
                print()
                need_retry = True
            if need_retry:
                try:
                    ps_install.main()
                except Exception:
                    print(retry_msg_2)
                    time.sleep(5)
                    print()
                    need_another_retry = True
            if need_another_retry:
                ps_install.main()
        else:
            show_basic_usage()
            show_install_usage()
    elif command == "commander" or command == "gui":
        from pythonselenium.console_scripts import ps_commander

        ps_commander.main()
    elif command == "behave-gui" or command == "gui-behave":
        from pythonselenium.console_scripts import ps_behave_gui

        ps_behave_gui.main()
    elif (
        command == "caseplans"
        or command == "case-plans"
        or command == "case_plans"
    ):
        from pythonselenium.console_scripts import ps_caseplans

        ps_caseplans.main()
    elif (
        command == "recorder"
        or (command == "record" and len(command_args) == 0)
    ):
        from pythonselenium.console_scripts import ps_recorder

        ps_recorder.main()
    elif (
        command == "mkrec"
        or command == "codegen"
        or (command == "record" and len(command_args) >= 1)
    ):
        if len(command_args) >= 1:
            from pythonselenium.console_scripts import ps_mkrec

            ps_mkrec.main()
        else:
            show_basic_usage()
            if command == "codegen":
                show_codegen_usage()
            else:
                show_mkrec_usage()
    elif command == "mkdir":
        if len(command_args) >= 1:
            from pythonselenium.console_scripts import ps_mkdir

            ps_mkdir.main()
        else:
            show_basic_usage()
            show_mkdir_usage()
    elif command == "mkfile":
        if len(command_args) >= 1:
            from pythonselenium.console_scripts import ps_mkfile

            ps_mkfile.main()
        else:
            show_basic_usage()
            show_mkfile_usage()
    elif command == "mkchart":
        if len(command_args) >= 1:
            from pythonselenium.console_scripts import ps_mkchart

            ps_mkchart.main()
        else:
            show_basic_usage()
            show_mkchart_usage()
    elif command == "convert":
        if len(command_args) == 1:
            from pythonselenium.utilities.selenium_ide import convert_ide

            convert_ide.main()
        else:
            show_basic_usage()
            show_convert_usage()
    elif command == "print":
        if len(command_args) >= 1:
            from pythonselenium.console_scripts import ps_print

            ps_print.main()
        else:
            show_basic_usage()
            show_print_usage()
    elif command == "extract-objects" or command == "extract_objects":
        if len(command_args) >= 1:
            from pythonselenium.console_scripts import ps_objectify

            ps_objectify.extract_objects()
        else:
            show_basic_usage()
            show_extract_objects_usage()
    elif command == "inject-objects" or command == "inject_objects":
        if len(command_args) >= 1:
            from pythonselenium.console_scripts import ps_objectify

            ps_objectify.inject_objects()
        else:
            show_basic_usage()
            show_inject_objects_usage()
    elif command == "objectify":
        if len(command_args) >= 1:
            from pythonselenium.console_scripts import ps_objectify

            ps_objectify.objectify()
        else:
            show_basic_usage()
            show_objectify_usage()
    elif command == "revert-objects" or command == "revert_objects":
        if len(command_args) >= 1:
            from pythonselenium.console_scripts import ps_objectify

            ps_objectify.revert_objects()
        else:
            show_basic_usage()
            show_revert_objects_usage()
    elif command == "encrypt" or command == "obfuscate":
        if len(command_args) >= 0:
            from pythonselenium.common import obfuscate

            obfuscate.main()
        else:
            show_basic_usage()
            show_encrypt_usage()
    elif command == "decrypt" or command == "unobfuscate":
        if len(command_args) >= 0:
            from pythonselenium.common import unobfuscate

            unobfuscate.main()
        else:
            show_basic_usage()
            show_decrypt_usage()
    elif command == "download":
        if len(command_args) >= 1 and command_args[0].lower() == "server":
            from pythonselenium.utilities.selenium_grid import download_selenium_server

            download_selenium_server.main(force_download=True)
        else:
            show_basic_usage()
            show_download_usage()
    elif command == "grid-hub" or command == "grid_hub":
        if len(command_args) >= 1:
            from pythonselenium.utilities.selenium_grid import grid_hub

            grid_hub.main()
        else:
            show_basic_usage()
            show_grid_hub_usage()
    elif command == "grid-node" or command == "grid_node":
        if len(command_args) >= 1:
            from pythonselenium.utilities.selenium_grid import grid_node

            grid_node.main()
        else:
            show_basic_usage()
            show_grid_node_usage()
    elif command == "version" or command == "--version":
        if len(command_args) == 0:
            from pythonselenium.console_scripts import logo_helper

            pythonselenium_logo = logo_helper.get_pythonselenium_logo()
            print(pythonselenium_logo)
            print("")
            show_package_location()
            show_version_info()
            print("")
        else:
            show_basic_usage()
    elif command == "methods" or command == "--methods":
        show_methods()
    elif command == "options" or command == "--options":
        show_options()
    elif command == "behave-options" or command == "--behave-options":
        show_behave_options()
    elif command == "proxy" or command == "--proxy":
        import os
        import warnings

        import fasteners

        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=UserWarning)
            pip_find_lock = fasteners.InterProcessLock(
                constants.PipInstall.FINDLOCK
            )
            with pip_find_lock:
                try:
                    from proxy import proxy  # noqa: F401
                except Exception:
                    shared_utils.pip_install(
                        "proxy.py", version=constants.ProxyPy.VER
                    )
            os.system("proxy %s" % " ".join(sys.argv[2:]))
    elif command == "help" or command == "--help":
        if len(command_args) >= 1:
            if command_args[0] == "get":
                print("")
                show_install_usage()
                return
            elif command_args[0] == "install":
                print("")
                show_install_usage()
                return
            elif command_args[0] == "commander":
                print("")
                show_commander_usage()
                return
            elif command_args[0] == "gui":
                print("")
                show_commander_usage()
                return
            elif command_args[0] == "behave-gui":
                print("")
                show_behave_gui_usage()
                return
            elif command_args[0] == "gui-behave":
                print("")
                show_behave_gui_usage()
                return
            elif command_args[0] == "caseplans":
                print("")
                show_caseplans_usage()
                return
            elif command_args[0] == "case-plans":
                print("")
                show_caseplans_usage()
                return
            elif command_args[0] == "case_plans":
                print("")
                show_caseplans_usage()
                return
            elif command_args[0] == "mkdir":
                print("")
                show_mkdir_usage()
                return
            elif command_args[0] == "mkfile":
                print("")
                show_mkfile_usage()
                return
            elif command_args[0] == "mkrec":
                print("")
                show_mkrec_usage()
                return
            elif command_args[0] == "codegen":
                print("")
                show_codegen_usage()
                return
            elif command_args[0] == "recorder":
                print("")
                show_recorder_usage()
                return
            elif command_args[0] == "mkchart":
                print("")
                show_mkchart_usage()
                return
            elif command_args[0] == "convert":
                print("")
                show_convert_usage()
                return
            elif command_args[0] == "print":
                print("")
                show_print_usage()
                return
            elif command_args[0] == "extract-objects":
                print("")
                show_extract_objects_usage()
                return
            elif command_args[0] == "inject-objects":
                print("")
                show_inject_objects_usage()
                return
            elif command_args[0] == "objectify":
                print("")
                show_objectify_usage()
                return
            elif command_args[0] == "revert-objects":
                print("")
                show_revert_objects_usage()
                return
            elif command_args[0] == "encrypt":
                print("")
                show_encrypt_usage()
                return
            elif command_args[0] == "obfuscate":
                print("")
                show_encrypt_usage()
                return
            elif command_args[0] == "decrypt":
                print("")
                show_decrypt_usage()
                return
            elif command_args[0] == "unobfuscate":
                print("")
                show_decrypt_usage()
                return
            elif command_args[0] == "download":
                print("")
                show_download_usage()
                return
            elif command_args[0] == "grid-hub":
                print("")
                show_grid_hub_usage()
                return
            elif command_args[0] == "grid-node":
                print("")
                show_grid_node_usage()
                return
        show_detailed_help()
    else:
        show_usage()
        c5 = colorama.Fore.RED + colorama.Back.LIGHTYELLOW_EX
        c7 = colorama.Fore.BLACK + colorama.Back.MAGENTA
        cr = colorama.Style.RESET_ALL
        invalid_cmd = "===> INVALID COMMAND: >> %s <<\n" % command
        invalid_cmd = invalid_cmd.replace(">> ", ">>" + c5 + " ")
        invalid_cmd = invalid_cmd.replace(" <<", " " + cr + "<<")
        invalid_cmd = invalid_cmd.replace(">>", c7 + ">>" + cr)
        invalid_cmd = invalid_cmd.replace("<<", c7 + "<<" + cr)
        print(invalid_cmd)


if __name__ == "__main__":
    main()
