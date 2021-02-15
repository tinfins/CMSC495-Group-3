import logging.config
import tkinter as tk
from tkinter import ttk


class StudentPage(tk.Frame):
    def __init__(self, master, controller):
        ttk.Frame.__init__(self, master)
        self.logger = logging.getLogger(__name__)
        self.master = master
        self.controller = controller
        self.master.title("Student Page")

        # Master frame for all widgets
        self.master_frame = ttk.Frame(self.master)
        # Frame for top window elements
        self.top_frame = ttk.Frame(self.master_frame)
        self.mid_frame = ttk.Frame(self.master_frame)
        spacer1 = ttk.Frame(self.master_frame, width=75, height=55)

        self.top_frame.pack(side=tk.TOP)
        self.mid_frame.pack(side=tk.TOP)

        label = ttk.Label(self.top_frame, text='Classes:')
        class_value = tk.StringVar(self.top_frame, 'CMSC 495-6380')
        self.classSubject = ttk.Combobox(self.top_frame, textvariable=class_value, state='readonly')

        # TODO: Populate this list dynamically from model
        self.classSubject['values'] = ('CMSC 495-6380',
                                  'SDEV 300-1234',
                                  'SDEV 460-5678'
                                  )

        view_label_frame = ttk.LabelFrame(self.mid_frame, text='Data View', height=600, width=800)

        label.grid(row=0, column=0, sticky='e', padx=5, pady=25)
        self.classSubject.grid(row=0, column=1, sticky='w', padx=15, pady=25)
        view_label_frame.pack(padx=75, pady=10)
        spacer1.pack(side=tk.BOTTOM)
