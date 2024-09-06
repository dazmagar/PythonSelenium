"""
Creates a new PythonSelenium chart presentation with boilerplate code.

Usage:
    pythonselenium mkchart [FILE.py] [LANG]
      or     pysel mkchart [FILE.py] [LANG]

Example:
    pysel mkchart new_chart.py --en

Language Options:
    --en / --English

Output:
    Creates a new PythonSelenium chart presentation.
    If the file already exists, an error is raised.
    By default, the slides are written in English,
    and use a "sky" theme with "slide" transition.
    The chart can be used as a basic boilerplate.
"""
import codecs
import colorama
import os
import sys


def invalid_run_command(msg=None):
    exp = "  ** mkchart **\n\n"
    exp += "  Usage:\n"
    exp += "          pythonselenium mkchart [FILE.py] [LANG]\n"
    exp += "          OR     pysel mkchart [FILE.py] [LANG]\n"
    exp += "  Example:\n"
    exp += "          pysel mkchart new_chart.py --en\n"
    exp += "  Language Options:\n"
    exp += "          --en / --English\n"
    exp += "  Output:\n"
    exp += "          Creates a new PythonSelenium chart presentation.\n"
    exp += "          If the file already exists, an error is raised.\n"
    exp += "          By default, the slides are written in English,\n"
    exp += '          and use a "sky" theme with "slide" transition.\n'
    exp += "          The chart can be used as a basic boilerplate.\n"
    if not msg:
        raise Exception("INVALID RUN COMMAND!\n\n%s" % exp)
    elif msg == "help":
        print("\n%s" % exp)
        sys.exit()
    else:
        raise Exception("INVALID RUN COMMAND!\n\n%s\n%s\n" % (exp, msg))


def main():
    c1 = ""
    c5 = ""
    c7 = ""
    cr = ""
    if "linux" not in sys.platform:
        if (
            "win32" in sys.platform
            and hasattr(colorama, "just_fix_windows_console")
        ):
            colorama.just_fix_windows_console()
        else:
            colorama.init(autoreset=True)
        c1 = colorama.Fore.BLUE + colorama.Back.LIGHTCYAN_EX
        c5 = colorama.Fore.RED + colorama.Back.LIGHTYELLOW_EX
        c7 = colorama.Fore.BLACK + colorama.Back.MAGENTA
        cr = colorama.Style.RESET_ALL

    help_me = False
    error_msg = None
    invalid_cmd = None
    language = "English"

    command_args = sys.argv[2:]
    file_name = command_args[0]
    if file_name == "-h" or file_name == "--help":
        invalid_run_command("help")
    elif not file_name.endswith(".py"):
        error_msg = 'File name must end with ".py"!'
    elif "*" in file_name or len(str(file_name)) < 4:
        error_msg = "Invalid file name!"
    elif file_name.startswith("-"):
        error_msg = 'File name cannot start with "-"!'
    elif "/" in str(file_name) or "\\" in str(file_name):
        error_msg = "File must be created in the current directory!"
    elif os.path.exists(os.getcwd() + "/" + file_name):
        error_msg = 'File "%s" already exists in this directory!' % file_name
    if error_msg:
        error_msg = c5 + "ERROR: " + error_msg + cr
        invalid_run_command(error_msg)

    if len(command_args) >= 2:
        options = command_args[1:]
        for option in options:
            option = option.lower()
            if option == "-h" or option == "--help":
                help_me = True
            elif option == "--en" or option == "--english":
                language = "English"
            else:
                invalid_cmd = "\n===> INVALID OPTION: >> %s <<\n" % option
                invalid_cmd = invalid_cmd.replace(">> ", ">>" + c5 + " ")
                invalid_cmd = invalid_cmd.replace(" <<", " " + cr + "<<")
                invalid_cmd = invalid_cmd.replace(">>", c7 + ">>" + cr)
                invalid_cmd = invalid_cmd.replace("<<", c7 + "<<" + cr)
                help_me = True
                break
    if help_me:
        invalid_run_command(invalid_cmd)

    dir_name = os.getcwd()
    file_path = "%s/%s" % (dir_name, file_name)
    html_name = file_name.replace(".py", ".html")
    class_name = "MyTestClass"
    item = "Item"
    select_option = "Select option"
    chart_options = '"pie", "bar", "column", "line", "area"'

    import_line = "from pythonselenium import BaseCase"
    main_line = "BaseCase.main(__name__, __file__)"
    parent_class = "BaseCase"
    class_line = "class %s(%s):" % (class_name, parent_class)
    settings = 'theme="sky", transition="slide"'
    chart_settings = 'title="Chart 1"'
    add_slide = '"<p>Chart Demo</p>" + self.extract_chart()'
    data = []
    data.append("%s" % import_line)
    data.append("%s" % main_line)
    data.append("")
    data.append("")
    data.append("%s" % class_line)
    data.append("    def test_chart_presentation(self):")
    data.append("        self.create_presentation(%s)" % settings)
    data.append("")
    data.append("        # %s => %s" % (select_option, chart_options))
    data.append("        self.create_pie_chart(%s)" % chart_settings)
    data.append('        self.add_data_point("%s A", 36)' % item)
    data.append('        self.add_data_point("%s B", 33)' % item)
    data.append('        self.add_data_point("%s C", 27)' % item)
    data.append('        self.add_data_point("%s D", 21)' % item)
    data.append('        self.add_data_point("%s E", 18)' % item)
    data.append('        self.add_data_point("%s F", 15)' % item)
    data.append("        self.add_slide(%s)" % add_slide)
    data.append("")
    data.append('        self.begin_presentation(filename="%s")' % html_name)
    data.append("")

    new_data = []
    if language == "English":
        new_data = data
    data = new_data
    file = codecs.open(file_path, "w+", "utf-8")
    file.writelines("\r\n".join(data))
    file.close()
    if " " not in file_name:
        os.system("pysel print %s -n" % file_name)
    elif '"' not in file_name:
        os.system('pysel print "%s" -n' % file_name)
    else:
        os.system("pysel print '%s' -n" % file_name)
    success = (
        "\n" + c1 + '* Chart Presentation: "' + file_name + '" was created! *'
        "" + cr + "\n"
    )
    print(success)


if __name__ == "__main__":
    invalid_run_command()
