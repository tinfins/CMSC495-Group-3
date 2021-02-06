#from big_teacher.src.gui import LoginGui
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import src.gui.LoginGui as LoginGui
from src.Settings import NoSettings
import logging.config

def main():
    logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
    root = ThemedTk(theme='arc', background=True)
    app = LoginGui.LoginGui(root)
    root.mainloop()


if __name__ == '__main__':
    check_settings = NoSettings.check_settings()
    if check_settings:
        main()
    else:
        NoSettings.create_logging_settings()
        logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
        logger = logging.getLogger(__name__)
        logger.info('config.ini file created')
        main()


