import logging.config
import MainApplication
import big_teacher.src.gui.HomePage as HomePage
import big_teacher.src.controller.MysqlConnector as MySqlConnector
import big_teacher.src.controller.StudentViewController as StudentViewController
import big_teacher.src.controller.LoginController as LoginController


class HomePageController:
    '''
    HomePage controller for application
    '''
    def __init__(self, master, controller, layout, engine, settings, prof):
        self.logger = logging.getLogger(__name__)
        self.master = master
        self.controller = controller
        self.layout = layout
        self.home_view = HomePage.HomePage(self.master, self.controller)
        self.settings = settings
        self.engine = engine
        self.prof_obj = prof

        # Set welcome_label
        self.home_view.welcome_label.config(text=f'Welcome, {self.prof_obj.prof_fname} {self.prof_obj.prof_lname}')

        # Set commands for Image buttons on HomePage
        self.home_view.img_panel1.bind('<Button-1>', lambda event: self.students_controller())
        self.home_view.img_panel3.bind('<Button-1>', lambda event: self.on_focus(event, self.assignments_controller))
        self.home_view.img_panel4.bind('<Button-1>', lambda event: self.on_focus(event, self.analysis_controller))
        self.home_view.logout_button.config(command=lambda: None)

    # Method used for label on-click events
    def on_focus(self, event, command):
        event.widget.focus_set()  # give keyboard focus to the label
        event.widget.bind('<Key>', lambda event: command)

    def students_controller(self):
        self.layout.status_bar.status_set('Students View selected')
        StudentViewController.StudentViewController(self.master, self, self.layout, self.engine, self.prof_obj)

    def assignments_controller(self):
        self.layout.status_bar.status_set('Assignments View selected')

    def analysis_controller(self):
        self.layout.status_bar.status_set('Analysis View selected')

    def logout(self):
        MySqlConnector.MysqlConnector.logout(self.engine)
        MySqlConnector.MysqlConnector.logout(self.engine, self.settings)
        LoginController.LoginController(self.master, self, self.layout)
