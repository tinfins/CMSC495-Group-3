# Standard imports
import logging.config
# Big Teacher module imports
import big_teacher.src.gui.LoginGui as LoginGui
import big_teacher.src.gui.MessageBox as MessageBox
import big_teacher.src.controller.Settings as Settings
import big_teacher.src.model.DataModel as DataModel
import big_teacher.src.controller.HomePageController as HomePageController
import big_teacher.src.controller.MysqlConnector as MysqlConnector


class LoginController:
    '''
    Login controller for application
    '''
    def __init__(self, master, controller, layout):
        '''
        Initializes LoginController and displays Login gui
        :params master:tk.Tk():master window
        :params controller:tk.obj:common controller for all views (MainApplication)
        :params layout:tk.Frame:MainLayout frame
        '''
        self.logger = logging.getLogger(__name__)
        self.master = master
        self.controller = controller
        self.layout = layout
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
        settings = Settings.Settings('config.ini')
        config_values = settings.db_config_read('sqldb')
        # Create settings model object
        settings_model = DataModel.SettingsModel(_dialect=config_values['db_type'], _username=username, _password=password, _host=config_values['host'], _port=config_values['port'], _db_name=config_values['db_name'])
        try:
            # Create engine
            db_engine = MysqlConnector.MysqlConnector.create_engine(settings_model)
            # Logs in via MysqlConnector and returns professorModel object
            prof = MysqlConnector.MysqlConnector.login(db_engine, settings_model)
            # Checks if prof object is populated or not
            if prof:
                self.layout.status_bar.status_set(f'{settings_model.username} logged in')
                self.logger.info(f"{settings_model.username} successfully logged in")
                self.login_view.master_frame.destroy()
                # Call HomePage Controller
                HomePageController.HomePageController(self.master, self, self.layout, db_engine, settings_model, prof)
            else:
                # Executes on failed login
                self.logger.warning(f"{settings_model.username} FAILED login attempt")
                MessageBox.MessageBox().onWarn('Invalid Login Credentials')
                self.layout.status_bar.status_set('Invalid Login Credentials')
        except:
            # Executes if there are no values to pass or sqldb section is missing from conifg.ini
            self.layout.status_bar.status_set('Unable to login. Check your configuration settings.')
            MessageBox.MessageBox().onInfo('Unable to login\nGo to Edit -> Settings and configure your database settings.')
