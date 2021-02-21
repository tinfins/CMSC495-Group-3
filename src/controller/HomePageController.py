import logging.config
# Big Teacher module imports
import src.gui.HomePage as HomePage


class HomePageController:
    '''
    HomePage controller for application
    '''
    def __init__(self, master, controller, layout, content_frame, engine, prof, data_frame):
        '''
        Initializes HomePageController and displays HomePage gui
        :params master:tk.Tk():master window
        :params controller:tk.obj:common controller for all views (MainApplication)
        :params layout:tk.Frame:MainLayout frame
        :params content_frame:Frame:content_frame to hold sub-windows
        :params engine:sql.engine:engine created during login
        :params settings:Obj:settings model
        :params prof:Obj:professor model
        :params data_frame:Obj:pandas data_frame
        '''
        self.logger = logging.getLogger(__name__)
        self.master = master
        self.controller = controller
        self.layout = layout
        self.content_frame = content_frame
        self.home_view = HomePage.HomePage(self.master, self.controller, self.content_frame)
        self.engine = engine
        self.prof = prof
        self.df = data_frame

        # Set commands for Image buttons on HomePage
        self.home_view.img_panel1.bind('<Button-1>', lambda event: self.students_controller())
        self.home_view.img_panel3.bind('<Button-1>', lambda event: self.assignments_controller())
        self.home_view.img_panel4.bind('<Button-1>', lambda event: self.analysis_controller())

    def students_controller(self):
        '''
        Sets status bar msg, forgets current page pack and opens selected page in label_frame
        '''
        self.controller.destroy_child_widgets()
        self.controller.student_frame()
        self.layout.status_bar.status_set('Students View selected')

    def assignments_controller(self):
        '''
        Sets status bar msg, forgets current page pack and opens selected page in label_frame
        '''
        self.controller.destroy_child_widgets()
        self.controller.assignments_frame()
        self.layout.status_bar.status_set('Assignments View selected')

    def analysis_controller(self):
        '''
        Sets status bar msg, forgets current page pack and opens selected page in label_frame
        '''
        self.controller.destroy_child_widgets()
        self.layout.status_bar.status_set('Analysis View selected')

    def close_window(self):
        self.home_view.master_frame.destroy()

'''
    def logout(self):
        MysqlConnector.MysqlConnector.logout(self.engine)
        MysqlConnector.MysqlConnector.logout(self.engine, self.settings)
        LoginController.LoginController(self.master, self, self.layout)
        '''
