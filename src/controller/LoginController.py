import logging.config
# Big Teacher module imports
import src.gui.LoginGui as LoginGui
import src.gui.MessageBox as MessageBox
from src.utils.Settings import Settings
import src.controller.MainPageController as MainPageController
from src.utils.Connector import Connector


class LoginController:
    '''
    Login controller for application
    '''
    def __init__(self, master, controller):
        '''
        Initializes LoginController and displays Login gui
        :params master:tk.Tk():master window
        :params controller:tk.obj:common controller for all views (MainApplication)
        :params layout:tk.Frame:MainLayout frame
        '''
        self.logger = logging.getLogger(__name__)
        self.master = master
        self.controller = controller
        self.login_view = LoginGui.LoginGui(self.master, self.controller)

        # Set commands for LoginGui buttons
        self.login_view.reset_button.config(command=self.reset_entries)
        self.login_view.login_button.config(command=self.login)

    def reset_entries(self):
        '''
        Reset entries for login page
        '''
        self.login_view.username.set('')
        self.login_view.password.set('')

    def login(self):
        '''
        Perform login function
        '''
        # Get username and password values from login_view
        username = self.login_view.username.get()
        password = self.login_view.password.get()
        # Read settings from config.ini file
        settings = Settings('config.ini')
        config_values = settings.db_config_read('sqldb')
        '''
        # Offline testing
        try:
            # Create engine
            self.connector = Connector(username, password, config_values)
            engine = self.connector.create_engine(self.connector.settings_model)
            conn = self.connector.login(engine)
            if conn:
                self.master.status_bar.status_set(f'{self.connector.settings_model.username} logged in')
                self.logger.info(f"{self.connector.settings_model.username} successfully logged in")
                '''
        self.login_view.master_frame.destroy()
        # Call MainPage Controller
        MainPageController.MainPageController(self.master, self.controller)
                                              # Offline testing
                                              #, self.connector)
        '''
        # Offline testing
            else:
                # Executes on failed login
                self.logger.warning(f"{self.connector.settings_model.username} FAILED login attempt")
                MessageBox.MessageBox().onWarn('Invalid Login Credentials')
                self.master.status_bar.status_set('Invalid Login Credentials')
        except:
            # Executes if there are no values to pass or sqldb section is missing from conifg.ini
            self.master.status_bar.status_set('Unable to login. Check your configuration settings.')
            MessageBox.MessageBox().onInfo('Unable to login\nGo to Edit -> Settings and configure your database settings.')
            '''
