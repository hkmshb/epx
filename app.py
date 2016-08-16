"""
ePinXtractr launcher.
"""

import sys
import os.path
import tkinter as tk



BASE_DIR = os.path.dirname(__file__)
sys.path.insert(0, BASE_DIR)


from epx.forms import ePinXtractr, AboutDialog


def launch():
    app = ePinXtractr(tk.Tk())
    app.display()


if __name__ == '__main__':
    launch()
