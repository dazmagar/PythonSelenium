""" Run this file using ``python recorder.py`` """

import os


def open_recorder_desktop_app():
    command = "pysel recorder"
    os.system(command)


if __name__ == "__main__":
    open_recorder_desktop_app()
