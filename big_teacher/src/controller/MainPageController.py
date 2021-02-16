import logging.config
# Big Teacher module imports
import big_teacher.src.gui.MainPage as MainPage
import big_teacher.src.controller.MysqlConnector as MysqlConnector
import big_teacher.src.controller.HomePageController as HomePageController
import big_teacher.src.controller.StudentPageController as StudentPageController
import big_teacher.src.controller.AssignmentsPageController as AssignmentsPageController
import big_teacher.src.controller.LoginController as LoginController


class MainPageController:
    '''
    HomePage controller for application
    '''

    def __init__(self, master=None, controller=None, layout=None, engine=None, settings=None, prof=None):
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
        self.main_view = MainPage.MainPage(self.master, self.controller)
        self.container = self.main_view.content_frame
        self.settings = settings
        self.engine = engine
        self.prof_obj = prof
        self.df = 'test'
            #MysqlConnector.MysqlConnector.get_data(self.engine, self.prof_obj)

        # Set welcome_label
        self.main_view.welcome_label.config(text=f'Welcome, {self.prof_obj.prof_fname} {self.prof_obj.prof_lname}')

        # Set logout button to logout
        self.main_view.logout_button.config(command=self.logout)

        # Set home button command
        self.main_view.home_button.config(command=lambda: self.show_frame('Home Page'))

        self.home_frame()

    def home_frame(self):
        self.main_view.view_label_frame.config(text='Home Page')
        # self.container.pack_forget()
        HomePageController.HomePageController(self.master, self, self.layout, self.container, self.engine,
                                              self.prof_obj, self.df)

    def student_frame(self):
        self.main_view.view_label_frame.config(text='Student View')
        # self.container.pack_forget()
        StudentPageController.StudentPageController(self.master, self, self.layout, self.container, self.engine,
                                                    self.prof_obj, self.df)

    def assignments_frame(self):
        self.main_view.view_label_frame.config(text='Assignments View')
        # self.container.pack_forget()
        AssignmentsPageController.AssignmentsPageController(self.master, self, self.layout,
                                                            self.main_view.content_frame, self.engine, self.prof_obj,
                                                            self.df)

        # self.frames['Analysis Page'] = AnalysisPageController.AnalysisPageController(self.master, self, self.layout, self.container, self.engine, self.prof_obj, self.df)

    def logout(self):
        '''
        Logout function.destroys previously created objects and brings back the login screen
        '''
        del self.settings
        del self.prof_obj
        self.engine.dispose()
        del self.engine
        self.main_view.master_frame.destroy()
        LoginController.LoginController(self.master, self, self.layout)

