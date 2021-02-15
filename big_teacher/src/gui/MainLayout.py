# Standard imports
import logging.config
import tkinter as tk
from tkinter import ttk
# Big Teacher module imports:
import big_teacher.src.gui.MenuStatus as MenuStatus


class MainLayout(tk.Frame):
    '''
    Main GUI layout of application. Contains Menu Bar and Status Bar
    '''
    def __init__(self, master, controller):
        '''
        Initialize Main Layout page
        '''
        ttk.Frame.__init__(self, master)
        self.logger = logging.getLogger(__name__)
        self.master = master
        self.controller = controller
        self.master.title('Big Teacher')
        self.pack()

        # Menu bar Frame
        self.menu_frame = ttk.Frame(self.master)
        # Main content frame
        self.content_frame = ttk.Frame(self.master)
        # Status bar frame
        self.status_frame = ttk.Frame(self.master)

        # Pack frames root window
        self.menu_frame.pack(side=tk.TOP, fill=tk.X)
        self.status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Instantiate menu bar
        menu_bar = MenuStatus.MenuBarGui(self.menu_frame, self.master)
        # Filler label
        filler_label = ttk.Label(self.content_frame)
        # Instantiate status bar
        self.status_bar = MenuStatus.StatusBar(self.status_frame)

        # Pack frames in root window
        menu_bar.pack()
        filler_label.pack()
        self.status_bar.pack()
