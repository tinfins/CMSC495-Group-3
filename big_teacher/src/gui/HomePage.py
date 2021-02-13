import tkinter as tk
from tkinter import ttk
import big_teacher.src.gui.MenuStatus as MenuStatus


class HomePage(tk.Frame):
    def __init__(self, master, controller):
        ttk.Frame.__init__(self, master)
        self.master = master

        # Frame for window elements
        self.top_frame = ttk.Frame(self.master)
        self.mid_frame = ttk.Frame(self.master)
        view_label_frame = ttk.LabelFrame(self.mid_frame, text='Home Page', height=600, width=800)
        self.content_frame = ttk.Frame(view_label_frame)
        spacer1 = ttk.Frame(self.master, width=75, height=55)

        # Pack root frame
        self.top_frame.pack(side=tk.TOP)
        self.mid_frame.pack(side=tk.TOP)
        self.content_frame.pack()

        # Welcome label
        # TODO: need to pass username to this widget
        label = ttk.Label(self.top_frame, text='Welcome, [username]')

        # TODO: Need to add images to contentFrame

        # Logout button
        logout_button = ttk.Button(self.top_frame, text='Logout', command=lambda: None)

        self.test_label = ttk.Label(self.content_frame, text='TEST PAGE', font=(None, 40))

        # Pack frames with widgets
        label.pack(padx=25, pady=10)
        logout_button.pack()
        view_label_frame.pack(padx=75, pady=10)
        self.test_label.pack()
        spacer1.pack(side=tk.BOTTOM)
