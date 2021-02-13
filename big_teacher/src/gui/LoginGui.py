import logging.config
import tkinter as tk
from tkinter import ttk
import big_teacher.src.gui.HomePage as HomePage
import big_teacher.src.gui.MessageBox as MessageBox
import big_teacher.src.Settings as Settings
import big_teacher.src.MysqlConnector as MysqlConnector


class LoginGui:
    '''
    Class displays Login window. Should only be opened as a TopLevel window
    '''
    def __init__(self, master, status_bar):
        self.master = master
        self.master.title("Big Teacher Login")
        self.status_bar = status_bar
        self.logger = logging.getLogger(__name__)

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

        # Pack GUI
        # Info Label packed in top_frame
        info_label.pack(padx=5, pady=35)
        # Grid layout for mid_frame
        username_label.grid(row=0, column=0, sticky='e', padx=10, pady=5)
        username_entry.grid(row=0, column=1, sticky='w', padx=10, pady=5)
        password_label.grid(row=1, column=0, sticky='e', padx=10, pady=5)
        password_entry.grid(row=1, column=1, sticky='w', padx=10, pady=5)
        # Grid layout for bottom_frame
        login_button.grid(row=0, column=0, sticky='e', padx=5, pady=25)
        reset_button.grid(row=0, column=2, columnspan=2, sticky='w', padx=5, pady=25)

    def login(self):
        # TODO: Refactor for modularity
        try:
            config_values = Settings.Settings('config.ini', 'sqldb').db_config_read()
            config_values['username'] = self.username.get()
            config_values['password'] = self.password.get()
            db_conn = MysqlConnector.MysqlConnector(config_values)
            if db_conn.login():
                self.logger.info(f"{config_values['username']} successfully logged in")
                self.status_bar.status_set(f"{config_values['username']} logged in")
                self.master_frame.destroy()
                HomePage.HomePage(self.master, self.status_bar)
            else:
                # Executes on failed login
                self.logger.warning(f"{config_values['username']} FAILED login attempt")
                MessageBox.MessageBox().onWarn('Invalid Login Credentials')
                self.status_bar.status_set('Invalid Login Credentials')
        except:
            # Executes if there are no values to pass or sqldb section is missing from conifg.ini
            self.status_bar.status_set('Unable to login. Check your configuration settings.')
            MessageBox.MessageBox().onInfo('Unable to login\nGo to Edit -> Settings and configure your database settings.')

    #def logout(self):
        #TODO:

    def reset_entries(self):
        self.username.set('')
        self.password.set('')

    def close_window(self):
        self.master.destroy()
