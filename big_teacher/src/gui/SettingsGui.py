import logging.config
import tkinter as tk
from tkinter import ttk
import sys
# Big Teacher module imports
import big_teacher.src.gui.MenuStatus as MenuStatus
import big_teacher.src.controller.Settings as Settings


class SettingsGui:
    '''
    Settings window should be opened as a TopLevel window, not in root window
    '''
    def __init__(self, master):
        '''
        Initialize Settings page
        '''
        self.master = master
        self.master.title('Big Teacher Settings')
        self.logger = logging.getLogger(__name__)

        # Main frame for LoginGui window
        self.master_frame = ttk.Frame(self.master)
        # Pack master_frame in window
        self.master_frame.pack()
        top_frame = ttk.Frame(self.master_frame)
        db_type_frame = ttk.Frame(self.master_frame)
        mid_frame = ttk.Frame(self.master_frame)
        bottom_frame = ttk.Frame(self.master_frame)
        self.status_frame = ttk.Frame(self.master_frame)
        # Spacer frames used for alignment
        spacer1 = ttk.Frame(self.master_frame, width=75, height=20)
        spacer2 = ttk.Frame(self.master_frame, width=75, height=20)

        # Pack frames in master frame
        self.status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        top_frame.pack(side=tk.TOP)
        db_type_frame.pack(side=tk.TOP)
        spacer1.pack(side=tk.LEFT)
        spacer2.pack(side=tk.RIGHT)
        mid_frame.pack(side=tk.TOP)
        bottom_frame.pack(side=tk.TOP)

        # Welcome Label
        info_label = ttk.Label(top_frame, text='Big Teacher Settings', justify='center', font=(None, 25))

        # Radio Button Group for database types
        self.db_type = tk.StringVar(db_type_frame, 'mysql')
        mysql_rb = ttk.Radiobutton(db_type_frame, text='MySQL', variable=self.db_type, value='mysql')
        pgsql_rb = ttk.Radiobutton(db_type_frame, text='PostgreSQL', variable=self.db_type, value='postgresql')
        oracle_rb = ttk.Radiobutton(db_type_frame, text='Oracle', variable=self.db_type, value='oracle')
        mssql_rb = ttk.Radiobutton(db_type_frame, text='MsSQL', variable=self.db_type, value='mssql')

        # Host label and entry
        host_label = ttk.Label(mid_frame, text='Host:')
        self.host = tk.StringVar()
        host_entry = ttk.Entry(mid_frame, textvariable=self.host, width=35)

        # Port label and entry
        port_label = ttk.Label(mid_frame, text='Port')
        self.port = tk.StringVar()
        port_entry = ttk.Entry(mid_frame, textvariable=self.port, width=35)

        # Database name label and entry
        db_name_label = ttk.Label(mid_frame, text='DB Name')
        self.db_name = tk.StringVar()
        db_name_entry = ttk.Entry(mid_frame, textvariable=self.db_name, width=35)

        # Save Button
        save_button = ttk.Button(bottom_frame, text='Save', command=lambda: self.save_settings())
        # Cancel Button
        cancel_button = ttk.Button(bottom_frame, text='Cancel', command=lambda: self.close_window())

        # Status Bar
        self.status_bar = MenuStatus.StatusBar(self.status_frame)

        # Pack Gui
        # Info label pack in top_frame
        info_label.pack(padx=75, pady=75)
        # Pack layout for db_type_frame
        mysql_rb.pack(side=tk.LEFT, padx=15, pady=15)
        pgsql_rb.pack(side=tk.LEFT, padx=15, pady=15)
        oracle_rb.pack(side=tk.LEFT, padx=15, pady=15)
        mssql_rb.pack(side=tk.LEFT, padx=15, pady=15)

        # Grid layout for mid_frame
        host_label.grid(row=0, column=0, sticky='e', padx=25, pady=5)
        host_entry.grid(row=0, column=1, sticky='w', padx=25, pady=5)
        port_label.grid(row=1, column=0, sticky='e', padx=25, pady=5)
        port_entry.grid(row=1, column=1, sticky='w', padx=25, pady=5)
        db_name_label.grid(row=2, column=0, sticky='e', padx=25, pady=5)
        db_name_entry.grid(row=2, column=1, sticky='w', padx=25, pady=5)

        # Grid layout for bottom_frame
        save_button.grid(row=0, column=0, sticky='e', padx=75, pady=15)
        cancel_button.grid(row=0, column=2, columnspan=2, sticky='w', padx=75, pady=15)

        # Status Bar packed in status_frame
        self.status_bar.pack()

        try:
            self.load_settings()
        except:
            error = sys.exc_info()[0]
            self.logger.error(f'Settings were not loaded - {error}')
            self.status_bar.status_set('Error encountered loading settings')

    def load_settings(self):
        '''
        Loads settings from file to populate settings page
        '''
        settings = Settings.Settings(config_file='config.ini').db_config_read(section='sqldb')
        self.db_type.set(settings['db_type'])
        self.host.set(settings['host'])
        self.port.set(settings['port'])
        self.db_name.set(settings['db_name'])
        self.logger.info(f'Settings successfully loaded from config.ini')
        self.status_bar.status_set(f'Settings successfully loaded from config.ini')

    def save_settings(self):
        '''
        Saves settings to file
        '''
        db_type = self.db_type.get()
        host = self.host.get()
        port = self.port.get()
        db_name = self.db_name.get()
        settings = Settings.Settings(config_file='config.ini')
        settings.db_config_write(section='sqldb', db_type=db_type, host=host, port=port, db_name=db_name)
        self.logger.info(f'config.ini {db_type} section updated')
        self.status_bar.status_set(f'config.ini {db_type} section updated')
        self.close_window()

    def close_window(self):
        '''
        Close window
        '''
        self.master.destroy()
