# Standard imports
import logging.config
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
# Big Teacher module imports:
import big_teacher.src.gui.HomePage as HomePage
import big_teacher.src.gui.LoginGui as LoginGui
import big_teacher.src.gui.MenuStatus as MenuStatus
import big_teacher.src.gui.MessageBox as MessageBox
import big_teacher.src.Settings as Settings
import big_teacher.src.MysqlConnector as MySqlConnector
import big_teacher.src.model.DataModel as DataModel


class MainApplication:
    """
    Main entry point of application
    """
    def __init__(self, master):
        self.logger = logging.getLogger(__name__)
        self.master = master

        # Menu bar Frame
        self.menu_frame = ttk.Frame(self.master)
        # Main content frame
        self.content_frame = ttk.Frame(self.master)
        # Status bar frame
        self.status_frame = ttk.Frame(self.master)

        # Pack frames root window
        self.menu_frame.pack(side=tk.TOP, fill=tk.X)
        self.status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Instantiate menu bar
        menu_bar = MenuStatus.MenuBarGui(self.menu_frame, self.master)
        # Filler label
        filler_label = ttk.Label(self.content_frame)
        # Instantiate status bar
        self.status_bar = MenuStatus.StatusBar(self.status_frame)

        # Pack frames in root window
        menu_bar.pack()
        filler_label.pack()
        self.status_bar.pack()

        # Open LoginGui
        self.login_view = LoginGui.LoginGui(self.master)
        self.login_view.login_button.config(command=self.login)
        self.login_view.reset_button.config(command=self.reset_entries)

        # Test Open Different Page Views
        #HomePage.HomePage(self.master, self.status_bar)
    
    def reset_entries(self):
        self.login_view.username.set('')
        self.login_view.password.set('')
    
    def login(self):
        username = self.login_view.username.get()
        password = self.login_view.password.get()
        settings = Settings.Settings('config.ini')
        config_values = settings.db_config_read('sqldb')
        # Create settings model object
        settings_model = DataModel.SettingsModel(_dialect=config_values['db_type'], _username=username, _password=password, _host=config_values['host'], _port=config_values['port'], _db_name=config_values['db_name'])
        try:
            db_conn = MySqlConnector.MysqlConnector(settings_model)
            if db_conn.login():
                self.status_bar.status_set(f'{settings_model.username} logged in')
                self.logger.info(f"{settings_model.username} successfully logged in")
                self.login_view.master_frame.destroy()
                HomePage.HomePage(self.master, self.status_bar)
            else:
                # Executes on failed login
                self.logger.warning(f"{settings_model.username} FAILED login attempt")
                MessageBox.MessageBox().onWarn('Invalid Login Credentials')
                self.status_bar.status_set('Invalid Login Credentials')
        except:
            # Executes if there are no values to pass or sqldb section is missing from conifg.ini
            self.status_bar.status_set('Unable to login. Check your configuration settings.')
            MessageBox.MessageBox().onInfo('Unable to login\nGo to Edit -> Settings and configure your database settings.')
        
        '''
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
            '''

def main():
    logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
    root = ThemedTk(theme='arc', background=True)
    app = MainApplication(root)
    root.mainloop()


if __name__ == '__main__':
    check_settings = Settings.NoSettings.check_settings()
    if check_settings:
        main()
    else:
        Settings.NoSettings.create_logging_settings()
        logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
        logger = logging.getLogger(__name__)
        main()
