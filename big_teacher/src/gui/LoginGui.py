import logging.config
import tkinter as tk
from tkinter import ttk
import big_teacher.src.gui.MenuStatus as MenuStatus
import big_teacher.src.gui.StudentView as DataView
import big_teacher.src.gui.MessageBox as MessageBox
import big_teacher.src.Settings as Settings
import big_teacher.src.MysqlConnector as MysqlConnector


class LoginGui:
    def __init__(self, master):
        self.master = master
        self.master.title("Big Teacher Login")
        self.logger = logging.getLogger(__name__)

        # Main frame for LoginGui window
        self.master_frame = ttk.Frame(self.master)
        # Pack master_frame in window
        self.master_frame.pack()
        menu_frame = ttk.Frame(self.master_frame)
        top_frame = ttk.Frame(self.master_frame)
        mid_frame = ttk.Frame(self.master_frame)
        bottom_frame = ttk.Frame(self.master_frame)
        self.status_frame = ttk.Frame(self.master_frame)
        # Spacer frames used for alignment
        spacer1 = ttk.Frame(self.master_frame, width=75, height=20)
        spacer2 = ttk.Frame(self.master_frame, width=75, height=20)

        menu_frame.pack(side=tk.TOP, fill=tk.X)
        self.status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        top_frame.pack()
        spacer1.pack(side=tk.LEFT)
        spacer2.pack(side=tk.RIGHT)
        mid_frame.pack()
        bottom_frame.pack()

        # Menu bar instantiate
        menu_bar = MenuStatus.MenuBarGui(menu_frame, self.master)

        # Welcome Label
        info_label = ttk.Label(top_frame, text='Welcome to Big Teacher!', justify='center', font=(None, 25))

        # Username label and entry
        username_label = ttk.Label(mid_frame, text='Username')
        self.username = tk.StringVar()
        username_entry = ttk.Entry(mid_frame, textvariable=self.username, width=35)

        # Password label and entry
        password_label = ttk.Label(mid_frame, text='Password')
        self.password = tk.StringVar()
        password_entry = ttk.Entry(mid_frame, textvariable=self.password, show='*', width=35)

        # Login Button
        login_button = ttk.Button(bottom_frame, text='Login', command=lambda: self.login())
        # Reset Button
        reset_button = ttk.Button(bottom_frame, text='Reset', command=lambda: self.reset_entries())

        # Status Bar instantiate
        self.status_bar = MenuStatus.StatusBar(self.status_frame)

        # Pack GUI
        # Menu Bar
        menu_bar.pack()
        # Info Label packed in top_frame
        info_label.pack(padx=75, pady=75)
        # Grid layout for mid_frame
        username_label.grid(row=0, column=0, sticky='e', padx=25, pady=5)
        username_entry.grid(row=0, column=1, sticky='w', padx=25, pady=5)
        password_label.grid(row=1, column=0, sticky='e', padx=25, pady=5)
        password_entry.grid(row=1, column=1, sticky='w', padx=25, pady=5)
        # Grid layout for bottom_frame
        login_button.grid(row=0, column=0, sticky='e', padx=75, pady=15)
        reset_button.grid(row=0, column=2, columnspan=2, sticky='w', padx=25, pady=75)
        # Status bar packed in status_frame
        self.status_bar.pack()

    def login(self):
        try:
            config_values = Settings.Settings('config.ini', 'sqldb').db_config_read()
            config_values['username'] = self.username.get()
            config_values['password'] = self.password.get()
            db_conn = MysqlConnector.MysqlConnector(config_values)
            if db_conn.login():
                self.logger.info(f"{config_values['username']} successfully logged in")
                self.status_bar.status_set(f"{config_values['username']} logged in")
                self.master.destroy()
            else:
                self.logger.warning(f"{config_values['username']} FAILED login attempt")
                MessageBox.MessageBox().onWarn('Invalid Login Credentials')
                self.status_bar.status_set('Invalid Login Credentials')
        except:
            self.status_bar.status_set('Unable to login. Check your configuration settings.')
            MessageBox.MessageBox().onInfo('Unable to login\nGo to Edit -> Settings and configure your database settings.')

    #def logout(self):
        #TODO:

    def reset_entries(self):
        self.username.set('')
        self.password.set('')

    def close_window(self):
        self.master.destroy()
