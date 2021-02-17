import logging.config
import tkinter as tk
from tkinter import ttk


class MainPage(tk.Frame):
    '''
    Class creates Main Page window.
    '''

    def __init__(self, master, controller):
        '''
        Initialize Main page
        '''
        ttk.Frame.__init__(self, master)
        self.logger = logging.getLogger(__name__)
        self.master = master
        self.controller = controller

        # Master frame for all widgets
        self.master_frame = ttk.Frame(self.master)
        # Frame for window elements
        self.top_frame = ttk.Frame(self.master_frame)
        self.mid_frame = ttk.Frame(self.master_frame)
        self.view_label_frame = ttk.LabelFrame(self.mid_frame, text='Home Page')
        self.content_frame = ttk.Frame(self.view_label_frame, width=800, height=600)
        self.bottom_frame = ttk.Frame(self.master_frame)

        # Pack root frame
        self.master_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.top_frame.pack(side=tk.TOP)
        self.mid_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.view_label_frame.pack(padx=75, pady=10)
        self.content_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.bottom_frame.pack(side=tk.BOTTOM)

        # Welcome label
        self.welcome_label = ttk.Label(self.top_frame)

        # Home button
        self.home_button = ttk.Button(self.top_frame, text='Home')

        # Logout button
        self.logout_button = ttk.Button(self.bottom_frame, text='Logout')

        # Pack frames with widgets
        self.welcome_label.pack(side=tk.LEFT, padx=25, pady=10)
        self.home_button.pack()
        self.logout_button.pack(padx=25, pady=25)
