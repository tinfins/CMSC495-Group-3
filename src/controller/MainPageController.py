import logging.config
# Big Teacher module imports
import src.gui.MainPage as MainPage
from src.utils.DatabaseQuery import DatabaseQuery
from src.utils.DataframeQueries import DataframeQueries
from src.gui.HomePage import HomePage
from src.gui.StudentPage import StudentPage
from src.gui.AssignmentsPage import AssignmentsPage
# Offline Testing
from src.model.DataModel import ProfessorModel


class MainPageController:
    '''
    HomePage controller for application
    '''

    def __init__(self, master, controller):
                 # Offline testing
                 #, connector):
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
        # Offline Testing
        #self.connector = connector
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
        # Offline Testing
        result = 'data-export.csv'
        #self.db_query = DatabaseQuery(self.connector.engine)
        self.df_query = DataframeQueries()
        # Offline Testing
        prof_obj = ProfessorModel(1, 'Jay', 'White', 'jwhite@umgc.edu')
        #prof_obj = self.db_query.get_prof(self.connector.settings_model)
        #result = self.db_query.get_data(prof_obj)
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
        self.home_page.img_panel3.bind('<Button-1>', lambda event: self.assignments_frame())
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
        table1 = self.get_table(self.student_page.class_subject.get(), self.student_page.tree_student, 's')
        table1.bind('<<TreeviewSelect>>', lambda event: self.tree_select(table1))
        # Combobox select event bind
        self.student_page.class_subject.bind('<<ComboboxSelected>>',
                                             lambda event: (self.destroy_child_widgets(table1), self.get_table(self.student_page.class_subject.get(), self.student_page.tree_student, 's')))
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
        '''
        # Display table based on course selected
        table1 = self.get_table(self.assignments_page.class_subject.get(), self.assignments_page.students_frame)
        table2 = self.get_table(self.assignments_page.class_subject.get(), self.assignments_page.assignments_frame)
        # Combobox select event bind
        
        self.assignments_page.class_subject.bind('<<ComboboxSelected>>',
                                             lambda event: (
                                             table1.close(), table2.close(), self.get_table(self.assignments_page.class_subject.get(), self.assignments_page.students_frame), self.get_table(self.assignments_page.class_subject.get(), self.assignments_page.assignments_frame)))
                                             '''
        return self.assignments_page

    def get_table(self, course, frame, f_type, index=None):
        # Display students table based on course selected
        if f_type == 's':
            table = self.df_query.get_students_df(course)
        if f_type == 'a':
            table = self.df_query.get_assignments(index)
        tree = self.display_tree(table, frame, f_type)
        return tree

    def display_tree(self, data_table, tree, f_type):
        '''
        Display table in pandastable tk widget
        :param data_table:pandas data frame
        :param frame:tkFrame to display pandastable widget
        '''
        tree.delete(*tree.get_children())
        cols = list(data_table.columns)
        tree['columns'] = cols
        for i in cols:
            tree.column(i, anchor="w")
            tree.heading(i, text=i, anchor='w')
        for index, row in data_table.iterrows():
            tree.insert("",0,text=index,values=list(row))
        tree['show'] = 'headings'
        return tree
    
    def tree_select(self, tree):
        cur_item = tree.focus()
        index = (tree.item(cur_item)['text'])+1
        index = int(index)
        table2 = self.get_table(self.student_page.class_subject.get(), self.student_page.tree_assignments, 'a', index)
        return table2

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

