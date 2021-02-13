import tkinter as tk


class SwitchWindow:
    def __init__(self, master):
        self.master = master

    def new_window(self, _class):
        new_window = tk.Toplevel(self.master)
        _class(new_window)
        new_window.tkraise()