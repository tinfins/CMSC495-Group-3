import logging.config
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class HomePage(tk.Frame):
    '''
    Class creates Home Page window.
    '''
    def __init__(self, master, controller):
        '''
        Initialize Home page
        '''
        ttk.Frame.__init__(self, master)
        self.logger = logging.getLogger(__name__)
        self.master = master
        self.controller = controller
        self.master.title("Big Teacher Home Page")

        # Master frame for all widgets
        self.master_frame = ttk.Frame(self.master)
        # Frame for window elements
        self.top_frame = ttk.Frame(self.master_frame)
        self.mid_frame = ttk.Frame(self.master_frame)
        self.view_label_frame = ttk.LabelFrame(self.mid_frame, text='Home Page')
        self.content_frame = ttk.Frame(self.view_label_frame)
        self.top_content_frame = ttk.Frame(self.content_frame)
        self.bottom_content_frame = ttk.Frame(self.content_frame)
        spacer1 = ttk.Frame(self.master_frame, width=75, height=50)
        spacer2 = ttk.Frame(self.content_frame, width=75, height=40)
        spacer3 = ttk.Frame(self.content_frame, width=75, height=40)
        spacer4 = ttk.Frame(self.content_frame, width=75, height=20)
        spacer5 = ttk.Frame(self.content_frame, width=75, height=20)

        # Pack root frame
        self.master_frame.pack()
        self.top_frame.pack(side=tk.TOP)
        self.mid_frame.pack(side=tk.TOP)
        spacer2.pack(side=tk.TOP)
        spacer3.pack(side=tk.BOTTOM)
        spacer4.pack(side=tk.LEFT)
        spacer5.pack(side=tk.RIGHT)
        self.top_content_frame.pack()
        self.bottom_content_frame.pack(side=tk.BOTTOM)

        # Welcome label
        self.welcome_label = ttk.Label(self.top_frame)

        # Create images and associated labels
        # Students image
        img1 = ImageTk.PhotoImage(Image.open("big_teacher/assets/Students.png").resize((250, 300), Image.ANTIALIAS))
        self.img_panel1 = ttk.Label(self.top_content_frame, image=img1)
        self.img_panel1.image = img1

        # Logo image
        img2 = ImageTk.PhotoImage(Image.open("big_teacher/assets/Logo.png").resize((250, 300), Image.ANTIALIAS))
        self.img_panel2 = ttk.Label(self.top_content_frame, image=img2)
        self.img_panel2.image = img2

        # Assignments image
        img3 = ImageTk.PhotoImage(Image.open("big_teacher/assets/Assignments.png").resize((250, 300), Image.ANTIALIAS))
        self.img_panel3 = ttk.Label(self.bottom_content_frame, image=img3)
        self.img_panel3.image = img3

        # Analysis image
        img4 = ImageTk.PhotoImage(Image.open("big_teacher/assets/Analysis.png").resize((250, 300), Image.ANTIALIAS))
        self.img_panel4 = ttk.Label(self.bottom_content_frame, image=img4)
        self.img_panel4.image = img4

        # Logout button
        self.logout_button = ttk.Button(self.top_frame, text='Logout')

        # Pack frames with widgets
        self.welcome_label.pack(side=tk.LEFT, padx=25, pady=10)
        self.logout_button.pack()
        self.view_label_frame.pack(padx=75, pady=10)
        self.content_frame.pack()
        self.img_panel1.pack(side=tk.LEFT, padx=50, pady=10)
        self.img_panel2.pack(side=tk.LEFT, padx=50, pady=10)
        self.img_panel3.pack(side=tk.LEFT, padx=50, pady=10)
        self.img_panel4.pack(side=tk.LEFT, padx=50, pady=10)
        spacer1.pack(side=tk.BOTTOM)
