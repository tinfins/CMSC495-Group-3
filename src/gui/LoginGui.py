import logging.config
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


class LoginGui(tk.Frame):
    '''
    Class creates Login window.
    '''
    def __init__(self, master, controller):
        '''
        Initialize Login page
        '''
        ttk.Frame.__init__(self, master)
        self.logger = logging.getLogger(__name__)
        self.master = master
        self.controller = controller
        self.controller.master.title("Big Teacher Login")

        # Master frame for all widgets
        self.master_frame = ttk.Frame(self.master)
        # Create frames for widget separation
        top_frame = ttk.Frame(self.master_frame)
        mid_frame = ttk.Frame(self.master_frame)
        bottom_frame = ttk.Frame(self.master_frame)
        # Spacer frames used for alignment
        spacer1 = ttk.Frame(self.master_frame, width=75, height=20)
        spacer2 = ttk.Frame(self.master_frame, width=75, height=20)

        # Pack master_frame with rest of frames
        self.master_frame.pack()
        top_frame.pack()
        spacer1.pack(side=tk.LEFT)
        spacer2.pack(side=tk.RIGHT)
        mid_frame.pack()
        bottom_frame.pack()
        
        img1 = ImageTk.PhotoImage(Image.open("src/assets/Logo.png").resize((50, 60), Image.ANTIALIAS))
        img_panel1 = ttk.Label(top_frame, image=img1)
        img_panel1.image = img1

        # Welcome Label
        info_label = ttk.Label(top_frame, text='Welcome to Big Teacher!', justify='center', font=(None, 16))

        # Username label and entry
        username_label = ttk.Label(mid_frame, text='Username')
        self.username = tk.StringVar()
        username_entry = ttk.Entry(mid_frame, textvariable=self.username, width=35)

        # Password label and entry
        password_label = ttk.Label(mid_frame, text='Password')
        self.password = tk.StringVar()
        password_entry = ttk.Entry(mid_frame, textvariable=self.password, show='*', width=35)

        # Login Button
        self.login_button = ttk.Button(bottom_frame, text='Login')
        # Reset Button
        self.reset_button = ttk.Button(bottom_frame, text='Reset')

        # Pack GUI
        # Info Label packed in top_frame
        info_label.pack(side=tk.LEFT, padx=25, pady=35)
        img_panel1.pack(side=tk.RIGHT, pady=15)
        # Grid layout for mid_frame
        username_label.grid(row=0, column=0, sticky='e', padx=10, pady=5)
        username_entry.grid(row=0, column=1, sticky='w', padx=10, pady=5)
        password_label.grid(row=1, column=0, sticky='e', padx=10, pady=5)
        password_entry.grid(row=1, column=1, sticky='w', padx=10, pady=5)
        # Grid layout for bottom_frame
        self.login_button.grid(row=0, column=0, sticky='e', padx=5, pady=25)
        self.reset_button.grid(row=0, column=2, columnspan=2, sticky='w', padx=5, pady=25)
