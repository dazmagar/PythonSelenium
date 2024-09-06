""" PythonSelenium Logo Processing  (for the console scripts interface)
    Logo generated from:
    http://www.patorjk.com/software/taag/#p=display&f=Slant&t=PythonSelenium """

import colorama
import sys

r"""
    ____        __  __               _____      __           _               
   / __ \__  __/ /_/ /_  ____  ____ / ___/___  / /__  ____  (_)_  ______ ___ 
  / /_/ / / / / __/ __ \/ __ \/ __ \\__ \/ _ \/ / _ \/ __ \/ / / / / __ `__ \
 / ____/ /_/ / /_/ / / / /_/ / / / /__/ /  __/ /  __/ / / / / /_/ / / / / / /
/_/    \__, /\__/_/ /_/\____/_/ /_/____/\___/_/\___/_/ /_/_/\__,_/_/ /_/ /_/ 
      /____/                                                                 
"""

def get_pythonselenium_logo():
    if (
        "win32" in sys.platform
        and hasattr(colorama, "just_fix_windows_console")
    ):
        colorama.just_fix_windows_console()
    else:
        colorama.init(autoreset=True)
    c1 = colorama.Fore.BLUE + colorama.Back.LIGHTCYAN_EX
    c2 = colorama.Fore.BLUE + colorama.Back.LIGHTGREEN_EX
    cr = colorama.Style.RESET_ALL
    ps = " "
    ps += cr
    ps += "\n"
    ps += c1
    ps += "    ____        __  __               _____      __           _                "
    ps += c2
    ps += " "
    ps += cr
    ps += "\n"
    ps += c1
    ps += "   / __ \\__  __/ /_/ /_  ____  ____ / ___/___  / /__  ____  (_)_  ______ ___  "
    ps += c2
    ps += " "
    ps += cr
    ps += "\n"
    ps += c1
    ps += "  / /_/ / / / / __/ __ \\/ __ \\/ __ \\\\__ \\/ _ \\/ / _ \\/ __ \\/ / / / / __ `__ \\ "
    ps += c2
    ps += " "
    ps += cr
    ps += "\n"
    ps += c1
    ps += " / ____/ /_/ / /_/ / / / /_/ / / / /__/ /  __/ /  __/ / / / / /_/ / / / / / / "
    ps += c2
    ps += " "
    ps += cr
    ps += "\n"
    ps += c1
    ps += "/_/    \\__, /\\__/_/ /_/\\____/_/ /_/____/\\___/_/\\___/_/ /_/_/\\__,_/_/ /_/ /_/  "
    ps += c2
    ps += " "
    ps += cr
    ps += "\n"
    ps += c1
    ps += "      /____/                                                                  "
    ps += c2
    ps += " "
    ps += cr
    ps += "\n"
    ps += cr
    return ps
