'''
SCRATCH GUI
By Sigton

This is a GUI built on Dylan5797's Scratch API
'''

import tkinter as tk
from tkinter import ttk

import scratchapi # Thanks to Dylan5797!

LARGE_FONT = ("Verdana", 12)

class ScratchGUIApp(tk.Tk):

    '''
    Main backend class, this is what makes stuff work.
    '''

    def __init__(self, *args, **kwargs):

        ''' Constructor '''

        # Call the parents constructor
        tk.Tk.__init__(self, *args, **kwargs)

        # Set the window title
        tk.Tk.wm_title(self, "Scratch GUI")

        # Set the window size
        self.geometry('{}x{}'.format(800,600))
