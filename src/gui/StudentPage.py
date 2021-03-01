import logging.config
import tkinter as tk
from tkinter import ttk


class StudentPage(tk.Frame):
    '''
    Class creates Student Page frame.
    '''
    def __init__(self, master, controller):
        '''
        Initialize Student page
        '''
        ttk.Frame.__init__(self, master)
        self.logger = logging.getLogger(__name__)
        self.master = master
        self.controller = controller

        # Master frame for all widgets
        self.master_frame = ttk.Frame(self.master)
        # Frame for top window elements
        self.top_frame = ttk.Frame(self.master_frame)
        self.mid_frame = ttk.Frame(self.master_frame)
        self.content_frame = ttk.Frame(self.master_frame)
        self.students_frame = ttk.Frame(self.content_frame)
        self.assignments_frame = ttk.Frame(self.content_frame, width=350, height=350)

        self.master_frame.pack()
        self.top_frame.pack(side=tk.TOP)
        self.mid_frame.pack(side=tk.TOP)
        self.content_frame.pack()
        self.students_frame.pack(side=tk.LEFT, padx=10, pady=10)
        self.assignments_frame.pack(side=tk.RIGHT, padx=10, pady=10)
        self.assignments_frame.pack_propagate(False)

        classes_label = ttk.Label(self.top_frame, text='Classes:')
        self.class_value = tk.StringVar()
        self.class_subject = ttk.Combobox(self.top_frame, textvariable=self.class_value, state='readonly')
        
        def create_treeview(frame):
            # Using treeview widget 
            treev = ttk.Treeview(frame, selectmode ='browse') 
            # Calling pack method w.r.to treeview 
            treev.pack(side ='right') 
            # Constructing vertical scrollbar 
            # with treeview 
            verscrlbar = ttk.Scrollbar(frame, orient ="vertical",  command = treev.yview) 
            # Calling pack method w.r.to verical  
            # scrollbar 
            verscrlbar.pack(side ='right', fill ='x') 
            # Configuring treeview 
            treev.configure(xscrollcommand = verscrlbar.set)
            return treev
        
        self.tree_student = create_treeview(self.students_frame)
        self.tree_assignments = create_treeview(self.assignments_frame)

        classes_label.pack(side=tk.LEFT, padx=25, pady=10)
        self.class_subject.pack()
