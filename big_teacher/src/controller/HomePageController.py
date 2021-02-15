import logging.config
import MainApplication
import big_teacher.src.gui.HomePage as HomePage
import big_teacher.src.controller.MysqlConnector as MysqlConnector
import big_teacher.src.controller.StudentPageController as StudentPageController
import big_teacher.src.controller.LoginController as LoginController


class HomePageController:
    '''
    HomePage controller for application
    '''
    def __init__(self, master, controller, layout, engine, settings, prof):
        '''
        Initializes HomePageController and displays HomePage gui
        :params master:tk.Tk():master window
        :params controller:tk.obj:common controller for all views (MainApplication)
        :params layout:tk.Frame:MainLayout frame
        :params engine:sql.engine:engine created during login
        :params settings:Obj:settings model
        :params prof:Obj:professor model
        '''
        self.logger = logging.getLogger(__name__)
        self.master = master
        self.controller = controller
        self.layout = layout
        self.home_view = HomePage.HomePage(self.master, self.controller)
        self.settings = settings
        self.engine = engine
        self.prof_obj = prof
        self.df = MysqlConnector.MysqlConnector.get_data(self.engine, self.prof_obj)

        # Set welcome_label
        self.home_view.welcome_label.config(text=f'Welcome, {self.prof_obj.prof_fname} {self.prof_obj.prof_lname}')

        # Set commands for Image buttons on HomePage
        self.home_view.img_panel1.bind('<Button-1>', lambda event: self.students_controller())
        self.home_view.img_panel3.bind('<Button-1>', lambda event: self.on_focus(event, self.assignments_controller))
        self.home_view.img_panel4.bind('<Button-1>', lambda event: self.on_focus(event, self.analysis_controller))
        self.home_view.logout_button.config(command=lambda: None)

    # Method used for label on-click events
    def on_focus(self, event, command):
        '''
        Uses click event on images to create an on-focus event and execute method passed as arg
        :params event:tk.event:event passed from selected event bind
        :params command:func:method passed with event
        '''
        event.widget.focus_set()  # give keyboard focus to the label
        event.widget.bind('<Key>', lambda event: command)

    def students_controller(self):
        '''
        Sets status bar msg, forgets current page pack and opens selected page in label_frame
        '''
        self.layout.status_bar.status_set('Students View selected')
        self.home_view.content_frame.pack_forget()
        StudentPageController.StudentPageController(self.master, self, self.layout, self.home_view.view_label_frame, self.engine, self.prof_obj, self.df)

    def assignments_controller(self):
        '''
        Sets status bar msg, forgets current page pack and opens selected page in label_frame
        '''
        self.layout.status_bar.status_set('Assignments View selected')

    def analysis_controller(self):
        '''
        Sets status bar msg, forgets current page pack and opens selected page in label_frame
        '''
        self.layout.status_bar.status_set('Analysis View selected')

'''
    def logout(self):
        MysqlConnector.MysqlConnector.logout(self.engine)
        MysqlConnector.MysqlConnector.logout(self.engine, self.settings)
        LoginController.LoginController(self.master, self, self.layout)
        '''
