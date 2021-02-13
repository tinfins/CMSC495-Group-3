import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import logging.config
import big_teacher.src.gui.HomePage as HomePage
import big_teacher.src.gui.LoginGui as LoginGui
import big_teacher.src.gui.MenuStatus as MenuStatus
from big_teacher.src.Settings import NoSettings


class MainApplication:
    """
    Main entry point of application
    """
    def __init__(self, master):
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
        LoginGui.LoginGui(self.master, self.status_bar)

        # Test Open Different Page Views
        #HomePage.HomePage(self.master, self.status_bar)


def main():
    logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
    root = ThemedTk(theme='arc', background=True)
    app = MainApplication(root)
    root.mainloop()


if __name__ == '__main__':
    check_settings = NoSettings.check_settings()
    if check_settings:
        main()
    else:
        NoSettings.create_logging_settings()
        logging.config.fileConfig(fname='config.ini', disable_existing_loggers=False)
        logger = logging.getLogger(__name__)
        main()
