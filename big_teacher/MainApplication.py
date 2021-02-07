import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import logging.config
import big_teacher.src.gui.LoginGui as LoginGui
import big_teacher.src.gui.StudentView as StudentView

logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)


class MainApplication:
    """
    Main entry point for GUI portion of application
    """
    def __init__(self, master):
        self.master = master
        
        # Container to stack frames
        self.container = ttk.Frame(self.master)
        self.container.pack(side="top", fill="both", expand=True)

        # Create frames
        self.frames = {}
        # Each view/page should be added as a frame in the style shown below
        self.frames["Student View"] = StudentView.StudentView(parent=self.container, controller=self.master)

        # Set frames in container
        # Each frame must have a layout in the style below
        self.frames["Student View"].pack()

        login_gui = SwitchWindow(master=self.master)
        login_gui.new_window(LoginGui.LoginGui, master=self.master)
        self.show_frame("Student View")


    def show_frame(self, page_name):
        '''
        Show a frame for the given page name
        '''
        frame = self.frames[page_name]
        # Shows menu on all views but the login view
        self.master.title(page_name)
        frame.tkraise()


class SwitchWindow:
    def __init__(self, master):
        self.master = master

    def new_window(self, _class, master):
        self.newWindow = tk.Toplevel(master)
        _class(self.newWindow)
    

if __name__ == "__main__":
    root = ThemedTk(theme='arc', background=True)
    app = MainApplication(root)
    root.mainloop()
