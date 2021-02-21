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
        self.layout.mainloop()

def main():
    '''
    Main entry point of application
    :return:
    '''
    logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
    logger = logging.getLogger(__name__)
    settings = Settings('config.ini')
    check_dir = settings.check_log_dir('logs')
    check_settings = settings.check_log_config(settings.config_file)
    if not check_dir or not check_settings:
        settings.create_log_settings(file='config.ini', directory='logs', dir_true=check_dir)
    logger.info('BigTeacher started')
    BigTeacher()


if __name__ == '__main__':
    main()
