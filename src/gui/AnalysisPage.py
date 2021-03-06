import logging.config
import tkinter as tk
from tkinter import ttk

# Plotting libraries
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import matplotlib.pyplot as plt
#import plotly.express as plotly
import numpy as np


class AnalysisPage(tk.Frame):
    '''
    Class creates Analysis Page frame.
    '''

    def __init__(self, master, controller):
        '''
        Initialize Graph page
        '''
        ttk.Frame.__init__(self, master)
        self.logger = logging.getLogger(__name__)
        self.master = master
        self.controller = controller

        # Master frame for all widgets
        self.master_frame = ttk.Frame(self.master)
        # Frame for top window elements
        self.right_frame = ttk.Frame(self.master_frame)
        self.mid_frame = ttk.Frame(self.master_frame)
        self.left_frame = ttk.Frame(self.master_frame)
        # self.content_frame = ttk.Frame(self.master_frame)

        # These frames will hold the labels and scroll bars
        self.classes_frame = ttk.Frame(self.left_frame)
        self.category_frame = ttk.Frame(self.left_frame)

        # These frames will hold the topics and options lists and graph area
        self.topic_frame = ttk.Frame(self.left_frame)
        self.options_frame = ttk.Frame(self.mid_frame)
        self.graph_frame = ttk.Frame(self.right_frame, width=400, height=400)

        # frame will hold the radio buttons
        self.radio_frame = ttk.Frame(self.mid_frame)

        self.master_frame.pack()
        self.right_frame.pack(side=tk.RIGHT)
        self.mid_frame.pack(side=tk.RIGHT)
        self.left_frame.pack(side=tk.LEFT)

        self.classes_frame.pack(side=tk.TOP, padx=10, pady=10)
        self.category_frame.pack(side=tk.TOP, padx=10, pady=10)

        self.topic_frame.pack(side=tk.BOTTOM, padx=10, pady=10)
        self.options_frame.pack(side=tk.BOTTOM, padx=10, pady=10)
        self.graph_frame.pack_propagate(False)
        self.graph_frame.pack(side=tk.BOTTOM, padx=10, pady=10, expand=False)

        self.radio_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

        # Class label and combobox
        classes_label = ttk.Label(self.classes_frame, text='Classes:')
        self.class_value = tk.StringVar()
        self.class_subject = ttk.Combobox(self.classes_frame, textvariable=self.class_value, state='readonly')

        # Topics label and combobox
        category_label = ttk.Label(self.category_frame, text='')

        # Radio Buttons
        self.radio_selection = tk.StringVar(self.radio_frame, 'bar')
        self.line_radio = ttk.Radiobutton(self.radio_frame, text="Line Graph", variable=self.radio_selection, value='line')
        self.scatter_radio = ttk.Radiobutton(self.radio_frame, text="Scatter Plot", variable=self.radio_selection, value='scatter')
        self.pie_radio = ttk.Radiobutton(self.radio_frame, text="Pie Chart   ", variable=self.radio_selection, value='pie')
        self.bar_radio = ttk.Radiobutton(self.radio_frame, text="Bar Graph  ", variable=self.radio_selection, value='bar')

        # This seems to create the table widgets themselves
        def create_treeview(frame):
            # Using treeview widget
            treev = ttk.Treeview(frame, selectmode='browse')
            # Calling pack method w.r.to treeview
            treev.pack(side='right')
            # Constructing vertical scrollbar
            # with treeview
            verscrlbar = ttk.Scrollbar(frame, orient="vertical", command=treev.yview)
            # Calling pack method w.r.to verical
            # scrollbar
            verscrlbar.pack(side='right', fill='x')
            # Configuring treeview
            treev.configure(xscrollcommand=verscrlbar.set)
            return treev

        self.tree_assignments = create_treeview(self.options_frame)
        self.tree_student = create_treeview(self.topic_frame)

        # Packing combo boxes
        classes_label.pack(side=tk.LEFT, padx=30, pady=10)
        self.class_subject.pack()
        category_label.pack(side=tk.LEFT, padx=25, pady=10)

        # Packing radio buttons
        self.line_radio.pack()
        self.scatter_radio.pack()
        self.pie_radio.pack()
        self.bar_radio.pack()

    # Plotting a line graph
    def plot_line(self, frame, asgn_type, data_frame, chart_type, index):
        # the figure that will contain the plot
        fig = plt.Figure(figsize=(3.5, 3.5), dpi=100)
        # adding the subplot
        ax = fig.add_subplot(111)
        if asgn_type == 'grades':
            plot = data_frame.plot(x='Assignments', y=index, ax=ax, kind=chart_type)
        elif asgn_type == 'asgn':
            plot = data_frame.plot(x='Name', y=index, ax=ax, kind=chart_type)
        plt.xticks(rotation=90)
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()

        # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, frame)
        toolbar.update()
        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()
