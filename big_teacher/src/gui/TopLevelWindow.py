import tkinter as tk


class SwitchWindow:
    '''
    Opens tk class in top level window
    '''
    def __init__(self, master):
        self.master = master

    def new_window(self, _class):
        '''
        Creates new top level window from _class with master
        :params _class:tk.Frame:class
        '''
        new_window = tk.Toplevel(self.master)
        _class(new_window)
        new_window.tkraise()
        