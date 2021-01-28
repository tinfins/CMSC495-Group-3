import tkinter as tk
from tkinter import ttk

#from functools import partial
LARGE_FONT = ("Verdana", 12)
class Test_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        label = ttk.Label(self,text='Test Page',font=LARGE_FONT)
        label.grid(row=1,column=0)
