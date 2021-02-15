import logging.config
import tkinter as tk
from tkinter import ttk


class StudentPage(tk.Frame):
    '''
    Class creates Student Page frame.
    '''
    def __init__(self, master, controller, content_frame):
        '''
        Initialize Student page
        '''
        ttk.Frame.__init__(self, master)
        self.logger = logging.getLogger(__name__)
        self.master = master
        self.controller = controller
        self.content_frame = content_frame
        self.master.title("Student Page")

        # Master frame for all widgets
        self.master_frame = ttk.Frame(self.content_frame)
        # Frame for top window elements
        self.top_frame = ttk.Frame(self.master_frame)
        self.mid_frame = ttk.Frame(self.master_frame)

        self.master_frame.pack()
        self.top_frame.pack(side=tk.TOP)
        self.mid_frame.pack(side=tk.TOP)

        classes_label = ttk.Label(self.top_frame, text='Classes:')
        self.class_value = tk.StringVar(self.top_frame, 'CMSC 495-6380')
        self.class_subject = ttk.Combobox(self.top_frame, textvariable=self.class_value, state='readonly')

        # TODO: Populate this list dynamically from model
        self.class_subject['values'] = ('CMSC 495-6380',
                                  'SDEV 300-1234',
                                  'SDEV 460-5678'
                                  )
        test_label = ttk.Label(self.mid_frame, text='Test Page', font=(None, 20))

        classes_label.pack(side=tk.LEFT, padx=25, pady=10)
        self.class_subject.pack()
        test_label.pack()
