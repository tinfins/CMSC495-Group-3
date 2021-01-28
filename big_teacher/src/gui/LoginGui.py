import tkinter as tk
from tkinter import ttk
#from functools import partial


class Login_Gui(tk.Frame):
    """
    Creates Login GUI frame with widgets
    """ 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        # Welcome Label
        infoLabel = ttk.Label(self, text="Welcome to Big Teacher!\nPlease enter your login\ncredentials to continue", justify="center")

        #username label and text entry box
        usernameLabel = ttk.Label(self, text="User Name")
        username = tk.StringVar()
        usernameEntry = ttk.Entry(self, textvariable=username)

        #password label and password entry box
        passwordLabel = ttk.Label(self,text="Password")
        password = tk.StringVar()
        passwordEntry = ttk.Entry(self, textvariable=password, show='*') 

        #login button
        loginButton = ttk.Button(self, text="Login", command=lambda: controller.show_frame("Test Page"), width=10)
        # Reset Button
        resetButton = ttk.Button(self,text="Reset",command=None, width=10)
        
        # Pack Gui
        infoLabel.grid(row=1, column=1, sticky='nsew', padx=25, pady=25, rowspan=3,  columnspan=4)
        usernameLabel.grid(row=4, column=0,  sticky='w', padx=25, pady=5)
        usernameEntry.grid(row=4, column=2, sticky='e', padx=25, pady=5)
        passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=5)
        passwordEntry.grid(row=5, column=2, sticky='e', padx=25, pady=5)
        loginButton.grid(row=6, column=0, sticky='nsew', padx=25, pady=15)
        resetButton.grid(row=6, column=2, columnspan=2, sticky='nsew', padx=25, pady=15)
        