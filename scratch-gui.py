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

        # Create the container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # And configure the grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Create a dictionary of frames and append all pages to it
        self.frames = {}

        for f in (LoginPage, MainPage):

            frame = f(container, self)

            self.frames[f] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        # Set the starting page
        self.show_frame(LoginPage)
