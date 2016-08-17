"""
ePinXtractr launcher.
"""

import os
import sys
import os.path


BASE_DIR = os.path.dirname(__file__)
sys.path.insert(0, BASE_DIR)

import tkinter as tk
from epx.forms import ePinXtractr, AboutDialog


def launch():
    app = ePinXtractr(tk.Tk())
    app.display()


if __name__ == '__main__':
    launch()
