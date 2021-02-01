import tkinter as tk
from tkinter import ttk


class Test_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        label = ttk.Label(self, text='Classes:')
        classValue = tk.StringVar()
        self.classSubject = ttk.Combobox(self, textvariable=classValue, state='readonly')

        self.classSubject['values'] = ('CMSC 495-6380',
                                  'SDEV 300-1234',
                                  'SDEV 460-5678'
                                  )

        self.classSubject.set('default')

        viewLabelFrame = ttk.LabelFrame(self, text='Data View', height=600, width=800)

        self.grid_columnconfigure(0, weight=1, uniform='column')
        self.grid_columnconfigure(1, weight=1, uniform='column')
        self.grid_columnconfigure(2, weight=1, uniform='column')
        label.grid(row=1,column=0, columnspan=2, padx=5, pady=25)
        self.classSubject.grid(row=1,column=1, padx=35, pady=25)
        viewLabelFrame.grid(row=3, column=0, rowspan=3, columnspan=15, padx=75, pady=75)
