import tkinter as tk
from tkinter import ttk
import logging.config
import big_teacher.src.gui.HomePage as HomePage


class MainView(tk.Frame):
    def __init__(self, master, controller):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller

        # Create frames
        self.frames = {}
        # Each view/page should be added as a frame in the style shown below
        self.frames['Unauthorized'] = UnauthorizedPage.UnauthorizedPage(master=self.master, controller=self.controller)
        self.frames['Home'] = HomePage.HomePage(master=self.master, controller=self.controller)

        # Pack frames
        self.frames['Unauthorized']
        self.frames['Home'].pack()

        login_gui = SwitchWindow(master=self.master)
        self.show_frame('Unauthorized')

    def show_frame(self, page_name):
        '''
        Show frame for the given page name
        '''
        frame = self.frames[page_name]
        self.controller.title(page_name)
        frame.tkraise()


class SwitchWindow:
    def __init__(self, master):
        self.master = master

    def new_window(self, _class):
        new_window = tk.Toplevel(self.master)
        _class(new_window)
        new_window.tkraise()
