# Standard imports
import logging.config
from ttkthemes import ThemedTk
# Big Teacher module imports:
import big_teacher.src.gui.MainLayout as MainLayout
import big_teacher.src.controller.LoginController as LoginController
import big_teacher.src.controller.Settings as Settings


class MainApplication:
    '''
    Main entry point of application
    '''
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
        self.master = ThemedTk(theme='arc', background=True)
        self.layout = MainLayout.MainLayout(self.master, self)
        # Each controller requires self.master, self, self.layout
        self.login_controller = LoginController.LoginController(self.master, self, self.layout)
        self.layout.mainloop()


if __name__ == '__main__':
    check_settings = Settings.NoSettings.check_settings()
    if check_settings:
        MainApplication()
    else:
        Settings.NoSettings.create_logging_settings()
        logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
        logger = logging.getLogger(__name__)
        MainApplication()
