"""Main TUI implementation for pyforecast

Author: Luke Welborn  
Created: 
"""


import py_cui

__version__ = 'v0.0.1'

class PyforecastApp:

    def __init__(self, master):

        self.master = master
        self.master.add_label('Hello py_cui!!!', 1, 1)


def main():
    root = py_cui.PyCUI(3, 3)
    wrapper =  PyforecastApp(root)
    root.start()
