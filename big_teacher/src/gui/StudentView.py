import tkinter as tk
from tkinter import ttk
import big_teacher.src.gui.MenuStatus as MenuStatus


class StudentView(tk.Frame):
    def __init__(self, master, controller):
        ttk.Frame.__init__(self, master)
        self.master = master

        # Frame for menu bar
        menu_frame = ttk.Frame(self.master)
        # Frame for top window elements
        self.top_frame = ttk.Frame(self.master)
        self.mid_frame = ttk.Frame(self.master)
        spacer1 = ttk.Frame(self.master, width=75, height=55)
        self.status_frame = ttk.Frame(self.master)

        menu_frame.pack(side=tk.TOP, fill=tk.X)
        self.status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.top_frame.pack(side=tk.TOP)
        self.mid_frame.pack(side=tk.TOP)

        menu_bar = MenuStatus.MenuBarGui(menu_frame, controller)

        label = ttk.Label(self.top_frame, text='Classes:')
        class_value = tk.StringVar(self.top_frame, 'CMSC 495-6380')
        self.classSubject = ttk.Combobox(self.top_frame, textvariable=class_value, state='readonly')

        # TODO: Populate this list dynamically from model
        self.classSubject['values'] = ('CMSC 495-6380',
                                  'SDEV 300-1234',
                                  'SDEV 460-5678'
                                  )

        view_label_frame = ttk.LabelFrame(self.mid_frame, text='Data View', height=600, width=800)

        # Status Bar instantiate
        self.status_bar = MenuStatus.StatusBar(self.status_frame)

        menu_bar.pack()
        label.grid(row=0, column=0, sticky='e', padx=5, pady=25)
        self.classSubject.grid(row=0, column=1, sticky='w', padx=15, pady=25)
        view_label_frame.pack(padx=75, pady=10)
        spacer1.pack(side=tk.BOTTOM)
        self.status_bar.pack()
