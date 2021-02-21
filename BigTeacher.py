# Standard imports
import logging.config
from ttkthemes import ThemedTk
# Big Teacher module imports:
import src.gui.MainLayout as MainLayout
import src.controller.LoginController as LoginController
from src.utils.Settings import Settings


class BigTeacher:
    '''
    Main class of application
    '''
    def __init__(self):
        '''
        Initializes tk.Tk() and starts mainloop
        '''
        logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
        self.logger = logging.getLogger(__name__)
        self.master = ThemedTk(theme='arc', background=True)
        self.layout = MainLayout.MainLayout(self.master, self)
        # Each controller requires self.master, self, self.layout
        self.login_controller = LoginController.LoginController(self.layout, self)
        self.logger.info('BigTeacher started')
        self.layout.mainloop()

def main():
    '''
    Main entry point of application
    :return:
    '''
    settings = Settings('config.ini')
    check_dir = settings.check_log_dir('src/logs/')
    check_settings = settings.check_log_config(settings.config_file)
    if not check_dir or not check_settings:
        settings.create_log_settings(file='config.ini', directory='src/logs/', dir_true=check_dir)
        settings.write_config(settings.config)
    BigTeacher()


if __name__ == '__main__':
    main()
