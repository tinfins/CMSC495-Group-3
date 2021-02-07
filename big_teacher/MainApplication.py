import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import os
import logging.config
import big_teacher.src.gui.MenuStatus as MenuStatus
import big_teacher.src.gui.LoginGui as LoginGui
import big_teacher.src.gui.DataView as DataView

logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)


class MainApplication(tk.Tk):
    """
    Main entry point for GUI portion of application
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Container to stack frames
        self.container = ttk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        print(os.getcwd())
        
        # Style application theme
        # Install ttkthemes (pip install ttkthemes)
        style = ThemedStyle(self)
        style.set_theme("breeze")

        # Create frames
        self.frames = {}
        # Each view/page should be added as a frame in the style shown below
        self.frames["Data View"] = DataView.Test_Page(parent=self.container, controller=self)
        
        # Set frames in container
        # Each frame must have a layout in the style below
        self.frames["Data View"].grid(row=1, column=0, sticky="nsew")
        
        self.show_frame("Data View")
        login_gui = LoginGui.SwitchWindow(master=self)
        login_gui.new_window(LoginGui.LoginGui, master=self)

        
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        # Shows menu on all views but the login view
        self.title(page_name)
        frame.tkraise()
    

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
    