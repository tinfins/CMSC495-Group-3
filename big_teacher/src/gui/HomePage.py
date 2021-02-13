import logging.config
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import big_teacher.src.gui.MenuStatus as MenuStatus


class HomePage(tk.Frame):
    def __init__(self, master, status_bar):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Big Teacher Home Page")
        self.status_bar = status_bar
        self.logger = logging.getLogger(__name__)

        # Master frame for all widgets
        self.master_frame = ttk.Frame(self.master)
        # Frame for window elements
        self.top_frame = ttk.Frame(self.master_frame)
        self.mid_frame = ttk.Frame(self.master_frame)
        view_label_frame = ttk.LabelFrame(self.mid_frame, text='Home Page')
        self.top_content_frame = ttk.Frame(view_label_frame)
        self.bottom_content_frame = ttk.Frame(view_label_frame)
        spacer1 = ttk.Frame(self.master_frame, width=75, height=50)
        spacer2 = ttk.Frame(view_label_frame, width=75, height=40)
        spacer3 = ttk.Frame(view_label_frame, width=75, height=40)
        spacer4 = ttk.Frame(view_label_frame, width=75, height=20)
        spacer5 = ttk.Frame(view_label_frame, width=75, height=20)

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
        # TODO: need to pass username to this widget
        label = ttk.Label(self.top_frame, text='Welcome, [username]')

        # Method used for label on-click events
        #TODO: Change page views based on widget name
        def on_focus(event, widget):
            event.widget.focus_set()  # give keyboard focus to the label
            event.widget.bind('<Key>', self.status_bar.status_set(f'{widget} image'))

        # Create images and associated labels
        # Students image
        img1 = ImageTk.PhotoImage(Image.open("big_teacher/assets/Students.png").resize((250, 300), Image.ANTIALIAS))
        img_panel1 = ttk.Label(self.top_content_frame, image=img1)
        img_panel1.image = img1

        img_panel1.bind('<Button-1>', lambda event: on_focus(event, 'Students'))

        # Logo image
        img2 = ImageTk.PhotoImage(Image.open("big_teacher/assets/Logo.png").resize((250, 300), Image.ANTIALIAS))
        img_panel2 = ttk.Label(self.top_content_frame, image=img2)
        img_panel2.image = img2

        img_panel2.bind('<Button-1>', lambda event: on_focus(event, 'Logo'))

        # Assignments image
        img3 = ImageTk.PhotoImage(Image.open("big_teacher/assets/Assignments.png").resize((250, 300), Image.ANTIALIAS))
        img_panel3 = ttk.Label(self.bottom_content_frame, image=img3, command=None)
        img_panel3.image = img3

        img_panel3.bind('<Button-1>', lambda event: on_focus(event, 'Assignments'))

        # Analysis image
        img4 = ImageTk.PhotoImage(Image.open("big_teacher/assets/Analysis.png").resize((250, 300), Image.ANTIALIAS))
        img_panel4 = ttk.Label(self.bottom_content_frame, image=img4, command=None)
        img_panel4.image = img4

        img_panel4.bind('<Button-1>', lambda event: on_focus(event, 'Analysis'))

        # Logout button
        logout_button = ttk.Button(self.top_frame, text='Logout', command=lambda: None)

        # Pack frames with widgets
        label.pack(side=tk.LEFT, padx=25, pady=10)
        logout_button.pack()
        view_label_frame.pack(padx=75, pady=10)
        img_panel1.pack(side=tk.LEFT, padx=50, pady=10)
        img_panel2.pack(side=tk.LEFT, padx=50, pady=10)
        img_panel3.pack(side=tk.LEFT, padx=50, pady=10)
        img_panel4.pack(side=tk.LEFT, padx=50, pady=10)
        spacer1.pack(side=tk.BOTTOM)
