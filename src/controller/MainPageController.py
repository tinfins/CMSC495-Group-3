import logging.config
from pandastable import Table, config
# Big Teacher module imports
import src.gui.MainPage as MainPage
from src.utils.DatabaseQuery import DatabaseQuery
from src.utils.DataframeQueries import DataframeQueries
from src.gui.HomePage import HomePage
from src.gui.StudentPage import StudentPage
from src.gui.AssignmentsPage import AssignmentsPage


class MainPageController:
    '''
    HomePage controller for application
    '''

    def __init__(self, master, controller, connector):
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
        self.connector = connector
        self.db_query = None
        self.df_query = None
        self.main_page = self.main_frame()
        self.home_page = None
        self.student_page = None
        self.assignments_page = None
        self.df = None

    def main_frame(self):
        '''
        Displays MainPage
        :return:tk.Frame:MainPage
        '''
        self.db_query = DatabaseQuery(self.connector.engine)
        self.df_query = DataframeQueries()
        prof_obj = self.db_query.get_prof(self.connector.settings_model)
        result = self.db_query.get_data(prof_obj)
        self.df = self.df_query.create_dataframe(result)
        self.main_page = MainPage.MainPage(self.master, self)
        # Set home button command
        self.main_page.home_button.config(command=lambda: None)
        # Set welcome_label
        self.main_page.welcome_label.config(text=f'Welcome, {prof_obj.prof_fname} {prof_obj.prof_lname}')
        # Set logout button to logout
        self.main_page.logout_button.config(command=self.logout)
        self.home_frame()
        return self.main_page

    def home_frame(self):
        '''
        Displays HomePage
        :return:tk.Frame:HomePage
        '''
        self.home_page = HomePage(self.main_page.content_frame, self)
        self.controller.master.title("Big Teacher Home Page")
        self.main_page.view_label_frame.config(text='Home Page')
        # Set commands for Image buttons on HomePage
        self.home_page.img_panel1.bind('<Button-1>', lambda event: self.students_frame())
        self.home_page.img_panel3.bind('<Button-1>', lambda event: None)
        self.home_page.img_panel4.bind('<Button-1>', lambda event: None)
        return self.home_page

    def students_frame(self):
        '''
        Displays StudentsPage
        :return:tk.Frame:StudentsPage
        '''
        self.destroy_child_widgets(self.main_page.content_frame)
        self.master.status_bar.status_set('Student View Selected')
        self.student_page = StudentPage(self.main_page.content_frame, self)
        self.controller.master.title('Student Page')
        self.main_page.home_button.config(command=lambda: (self.destroy_child_widgets(self.main_page.content_frame), self.home_frame()))
        # Dynamically set course combobox
        self.student_page.class_subject['values'] = self.df_query.get_classes()
        self.student_page.class_subject.current(0)
        # Display table based on course selected
        self.display_table(self.student_page.class_subject.get())
        # Combobox select event bind
        self.student_page.class_subject.bind('<<ComboboxSelected>>',
                                             lambda event: self.display_table(self.student_page.class_subject.get()))
        return self.student_page

    def assignments_frame(self):
        '''
        Displays AssignmentsPage
        :return:tk.Frame:AssignmentsPage
        '''
        self.destroy_child_widgets(self.main_page.content_frame)
        self.master.status_bar.status_set('Assignments View Selected')
        self.assignments_page = AssignmentsPage(self.main_page.content_frame, self)
        self.controller.master.title('Assignments Page')
        self.main_page.home_button.config(
            command=lambda: (self.destroy_child_widgets(self.main_page.content_frame), self.home_frame()))
        # Dynamically set course combobox
        self.assignments_page.class_subject['values'] = self.df_query.get_classes()
        self.assignments_page.class_subject.current(0)
        # Display table based on course selected
        self.display_table(self.assignments_page.class_subject.get())
        # Combobox select event bind
        self.assignments_page.class_subject.bind('<<ComboboxSelected>>',
                                             lambda event: self.display_table(self.assignments_page.class_subject.get()))
        return self.assignments_page

    def display_table(self, course):
        '''
        Display table in pandastable tk widget
        :param course:String:course name
        '''
        data_table = self.df_query.get_table(course, self.df)

        pt = Table(self.student_page.mid_frame, dataframe=data_table, showtoolbar=True, width=800, height=600)
        options = {'fontsize': 8}
        config.apply_options(options, pt)
        pt.show()

    def close_window(self):
        self.main_page.master_frame.destroy()

    def destroy_child_widgets(self, container):
        for child in container.winfo_children():
            child.destroy()

    def logout(self):
        '''
        Logout function.destroys previously created objects and brings back the login screen
        '''
        self.connector.engine.dispose()
        del self.db_query
        del self.df
        del self.main_page
        self.destroy_child_widgets(self.master)
        self.master.status_bar.status_set(f'{self.connector.settings_model.username} logged out')
        self.logger.info(f"{self.connector.settings_model.username} logged out")
        del self.connector
        from src.controller.LoginController import LoginController
        LoginController(self.controller.layout, self.controller)

