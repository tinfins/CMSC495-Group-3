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
        infoLabel = ttk.Label(self, text="Welcome to Big Teacher!\nPlease enter your login credentials to continue", justify="center", font=(None, 20))

        #username label and text entry box
        usernameLabel = ttk.Label(self, text="User Name", font=(None, 14))
        username = tk.StringVar()
        usernameEntry = ttk.Entry(self, textvariable=username)

        #password label and password entry box
        passwordLabel = ttk.Label(self,text="Password", font=(None, 14))
        password = tk.StringVar()
        passwordEntry = ttk.Entry(self, textvariable=password, show='*') 

        #login button
        loginButton = ttk.Button(self, text="Login", command=lambda: controller.show_frame("Test Page"), width=10)
        # Reset Button
        resetButton = ttk.Button(self,text="Reset",command=None, width=10)
        
        # Pack Gui
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1, uniform='column')
        self.grid_columnconfigure(2, weight=1, uniform='column')
        self.grid_rowconfigure(4, weight=1, uniform='row')
        self.grid_rowconfigure(5, weight=1, uniform='row')
        self.grid_rowconfigure(6, weight=1, uniform='row')
        infoLabel.grid(row=0, column=1, sticky='e', padx=25, pady=25, rowspan=3,  columnspan=2)
        usernameLabel.grid(row=4, column=1, sticky='e', padx=5, pady=15)
        usernameEntry.grid(row=4, column=2, sticky='w', padx=5, pady=15)
        passwordLabel.grid(row=5, column=1, sticky='e', padx=5, pady=15)
        passwordEntry.grid(row=5, column=2, sticky='w', padx=5, pady=15)
        loginButton.grid(row=6, column=0, columnspan=2, sticky='ne', padx=10, pady=15)
        resetButton.grid(row=6, column=2, sticky='nw', padx=10, pady=15)
        