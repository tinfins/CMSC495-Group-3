import logging.config
import tkinter as tk
from tkinter import ttk

# Plotting libraries
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
import matplotlib.pyplot as plotter
import plotly.express as plotly
import numpy as np
from pandas import DataFrame



class AnalysisPage(tk.Frame):
    '''
    Class creates Analysis Page frame.
    '''


    # Plotting a line graph
    def plot_line(self, graph, canvas, x_title, y_title, x_values, y_values, title):
        graph.clear()
        graph.plot(x_values, y_values)
        graph.set_xlabel(x_title)
        graph.set_ylabel(y_title)
        graph.set_title(title)
        canvas.draw()

    # Plotting a scatter
    def plot_scatter(self, graph, canvas, x_title, y_title, x_values, y_values, title):
        graph.clear()
        graph.scatter(x_values, y_values, color='g')
        graph.set_xlabel(x_title)
        graph.set_ylabel(y_title)
        graph.set_title(title)
        canvas.draw()

    # Plotting a bar
    def plot_bar(self, graph, canvas, data_frame, df_title1, df_title2, title):
        graph.clear()
        df_graph = data_frame[[df_title1, df_title2]].groupby(df_title1).sum()
        df_graph.plot(kind='bar', legend=True, ax=graph)
        graph.set_title(title)
        canvas.draw()

    # Plotting a pie
    def plot_pie(frame, graph, canvas, data_frame, title):
        graph.clear()
        data_frame.plot.pie(y=title, figsize=(5, 5), autopct='%1.1f%%', startangle=90, ax = graph)
        plotter.show()
        canvas.draw()

    def draw_graph(self, plot_line, plot_scatter, plot_bar, plot_pie):
        if str(self.radio_select.get()) == "Line Graph":
            plot_line(self.graph, self.canvas, "x stuff", "y stuff", [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], "title stuff")

        elif str(self.radio_select.get()) == "Scatter Plot":
            plot_scatter(self.graph, self.canvas, "x stuff", "y stuff", [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], "title stuff")

        elif str(self.radio_select.get()) == "Pie Chart   ":
            plot_pie(self.graph, self.canvas, DataFrame({'Year': [1950,1960,1970]},index=['Year1','Year2']), "pie chart")

        else:#if str(self.radio_select.get()) == "Bar Graph  ":
            plot_bar(self, self.graph, self.canvas, DataFrame({'Year': [1950,1960,1970],'Unemployment_Rate': [6.2,5.5,6.3]}, columns=['Year','Unemployment_Rate']),'Year', 'Unemployment_Rate', "Bar graph title")




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
        self.graph_frame = ttk.Frame(self.right_frame)

        # frame will hold the radio buttons
        self.radio_frame = ttk.Frame(self.mid_frame)

        self.master_frame.pack()
        self.right_frame.pack(side=tk.RIGHT)
        self.mid_frame.pack(side=tk.RIGHT)
        self.left_frame.pack(side=tk.LEFT)

        self.classes_frame.pack(side=tk.TOP, padx=10, pady=25)
        self.category_frame.pack(side=tk.TOP, padx=10, pady=10)

        self.topic_frame.pack(side=tk.BOTTOM, padx=10, pady=10)
        self.options_frame.pack(side=tk.BOTTOM, padx=10, pady=10)
        self.graph_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

        self.radio_frame.pack(side=tk.BOTTOM, padx=10, pady=10)

        # Class label and combobox
        classes_label = ttk.Label(self.classes_frame, text='Classes:')
        self.class_value = tk.StringVar()
        self.class_subject = ttk.Combobox(self.classes_frame, textvariable=self.class_value, state='readonly')

        # Figure and Canvas for graphing area
        figure = Figure(figsize=(4.2, 4.2), dpi=100)
        self.graph = figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(figure, self.graph_frame)
        toolbar = NavigationToolbar2Tk(self.canvas, self.graph_frame)
        toolbar.update()
        self.canvas.get_tk_widget().pack()


        # Radio Buttons
        self.radio_select = tk.StringVar()
        self.line_radio = ttk.Radiobutton(self.radio_frame, text="Line Graph", variable=self.radio_select, value=1,
                                         command=self.draw_graph(self.plot_line, self.plot_scatter, self.plot_bar, self.plot_pie))

        self.scatter_radio = ttk.Radiobutton(self.radio_frame, text="Scatter Plot", variable=self.radio_select, value=2,
                                         command=self.draw_graph(self.plot_line, self.plot_scatter, self.plot_bar, self.plot_pie))

        self.pie_radio = ttk.Radiobutton(self.radio_frame, text="Pie Chart   ", variable=self.radio_select, value=3,
                                         command=self.draw_graph(self.plot_line, self.plot_scatter, self.plot_bar, self.plot_pie))

        self.bar_radio = ttk.Radiobutton(self.radio_frame, text="Bar Graph  ", variable=self.radio_select, value=4,
                                         command=self.draw_graph(self.plot_line, self.plot_scatter, self.plot_bar, self.plot_pie))

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

        # Packing radio buttons
        self.line_radio.pack()
        self.scatter_radio.pack()
        self.pie_radio.pack()
        self.bar_radio.pack()

