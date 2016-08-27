'''
SCRATCH GUI
By Sigton

This is a GUI built on Dylan5797's Scratch API
'''

import tkinter as tk
from tkinter import ttk

import scratchapi

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

        # Create the container
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        # And configure the grid
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Create a dictionary of frames and append all pages to it
        self.frames = {}

        for f in (LoginPage, MenuPage):

            frame = f(self.container, self)

            self.frames[f] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        # Set the starting page
        self.show_frame(LoginPage)

    def show_frame(self, cont):

        # A simple function to switch pages

        frame = self.frames[cont]
        frame.tkraise()

class LoginPage(tk.Frame):

    '''
    This is all content on the login page
    '''

    def __init__(self, parent, controller):

        ''' Constructor '''

        # Call the parents constructor
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

        # Add the title
        self.title = ttk.Label(self, text="Log in to your Scratch account", font=LARGE_FONT)
        self.title.grid(row=0,column=0,columnspan=2,pady=10)

        # Add the login form
        self.usernameTag = ttk.Label(self, text="Username:")
        self.usernameTag.grid(row=1,column=0,sticky="e",pady=2)
        self.usernameEntry = ttk.Entry(self)
        self.usernameEntry.grid(row=1,column=1,pady=2)
        self.passwordTag = ttk.Label(self, text="Password:")
        self.passwordTag.grid(row=2,column=0,sticky="e",pady=2)
        self.passwordEntry = ttk.Entry(self)
        self.passwordEntry.grid(row=2,column=1,pady=2)

        # Just in case theres anything to report
        self.errorMessage = ttk.Label(self, text="", foreground="red")
        self.errorMessage.grid(row=3,column=0,columnspan=2,pady=5)

        # Add the disclaimer
        self.subtitle = ttk.Label(self, text="Account information is not collected in any way.")
        self.subtitle.grid(row=4,column=0,columnspan=2)

        # And finally add the login button
        self.button = ttk.Button(self, text="Login",
                                 command= lambda: self.login())
        self.button.grid(row=5,column=0,columnspan=2,pady=10)

    def login(self):

        # Attempts to log the user in to the scratchapi

        usernameData = self.usernameEntry.get()
        passwordData = self.passwordEntry.get()

        if usernameData == "" or passwordData == "":
            # Stop the function if the fields are empty.
            self.errorMessage.config(text="These fields are required.")
            return

        # Attempt to login to the scratchapi with the given username and password

        try:
            scratch = scratchapi.ScratchUserSession(usernameData, passwordData)
        except:
            # Stop the function if there was an error
            self.errorMessage.config(text="Login failed.")
            return

        self.controller.show_frame(MenuPage)
    
class MenuPage(tk.Frame):

    '''
    This is all content on the main page.
    '''

    def __init__(self, parent, controller):

        ''' Constructor '''

        # Call the parents constructor
        tk.Frame.__init__(self, parent)

        self.parent = parent
        self.controller = controller

app = ScratchGUIApp()
app.mainloop()
