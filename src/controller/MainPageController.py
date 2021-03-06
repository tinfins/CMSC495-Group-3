import logging.config
# Big Teacher module imports
import src.gui.MainPage as MainPage
from src.utils.DatabaseQuery import DatabaseQuery
from src.utils.DataframeQueries import DataframeQueries
from src.gui.HomePage import HomePage
from src.gui.StudentPage import StudentPage
from src.gui.AssignmentsPage import AssignmentsPage
from src.gui.AnalysisPage import AnalysisPage
# Offline testing
from src.model.DataModel import ProfessorModel


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
        self.analysis_page = None
        self.index = None
        self.cur_item = None
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
        self.home_page.img_panel3.bind('<Button-1>', lambda event: self.assignments_frame())
        self.home_page.img_panel4.bind('<Button-1>', lambda event: self.analysis_frame())
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
        self.main_page.view_label_frame.config(text='Students Page')
        self.main_page.home_button.config(command=lambda: (self.destroy_child_widgets(self.main_page.content_frame), self.home_frame()))
        # Dynamically set course combobox
        self.student_page.class_subject['values'] = self.df_query.get_classes()
        self.student_page.class_subject.current(0)
        table1 = self.get_table(self.student_page.class_subject.get(), self.student_page.tree_student, 's')
        table1.bind('<<TreeviewSelect>>', lambda event: (self.tree_select(table1), self.get_table(self.student_page.class_subject.get(), self.student_page.tree_assignments, 'a', self.index, "grades")))
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
        self.main_page.view_label_frame.config(text='Assignments Page')
        self.main_page.home_button.config(
            command=lambda: (self.destroy_child_widgets(self.main_page.content_frame), self.home_frame()))
        # Dynamically set course combobox
        self.assignments_page.class_subject['values'] = self.df_query.get_classes()
        self.assignments_page.class_subject.current(0)
        table1 = self.get_table(self.assignments_page.class_subject.get(), self.assignments_page.tree_assignments, 'a', None, 'ind')
        table1.bind('<<TreeviewSelect>>', lambda event: (self.tree_select(table1), self.get_table(self.assignments_page.class_subject.get(), self.assignments_page.tree_student, 'a', self.index, "asgn")))
        self.assignments_page.class_subject.bind('<<ComboboxSelected>>', lambda event: (self.destroy_child_widgets(table1), self.get_table(self.assignments_page.class_subject.get(), self.assignments_page.tree_assignments, 'a', None, "ind")))
        return self.assignments_page

    def analysis_frame(self):
        '''
        Displays AssignmentsPage
        :return:tk.Frame:AssignmentsPage
        '''
        self.destroy_child_widgets(self.main_page.content_frame)
        self.master.status_bar.status_set('Assignments View Selected')
        self.analysis_page = AnalysisPage(self.main_page.content_frame, self)
        self.controller.master.title('Analysis Page')
        self.main_page.view_label_frame.config(text='Analysis Page')
        self.main_page.home_button.config(
            command=lambda: (self.destroy_child_widgets(self.main_page.content_frame), self.home_frame()))
        # Dynamically set course combobox
        self.analysis_page.class_subject['values'] = self.df_query.get_classes()
        self.analysis_page.class_subject.current(0)
        table1 = self.get_table(self.analysis_page.class_subject.get(), self.analysis_page.tree_student, 's')
        table2 = self.get_table(self.analysis_page.class_subject.get(), self.analysis_page.tree_assignments, 'a',
                                None, 'ind')
        table1.bind('<<TreeviewSelect>>', lambda event: (self.tree_select(table1), self.chart_plot(self.analysis_page.class_subject.get(), 'grades', self.analysis_page.radio_selection.get(), self.index)))
        table2.bind('<<TreeviewSelect>>', lambda event: (self.tree_select(table2), self.chart_plot(self.analysis_page.class_subject.get(), 'asgn', self.analysis_page.radio_selection.get(), self.index)))
        self.analysis_page.class_subject.bind('<<ComboboxSelected>>', lambda event: (self.destroy_child_widgets(table1), self.destroy_child_widgets(table2), self.get_table(self.analysis_page.class_subject.get(), self.analysis_page.tree_student, 's'), self.get_table(self.analysis_page.class_subject.get(), self.analysis_page.tree_assignments, 'a', None, 'ind')))
        return self.analysis_page

    def get_table(self, course, frame, f_type, index=None, asgn_type=None):
        '''
        Uses DataframeQueries to get requested table
        :param course: Course name from combobox
        :param frame: tk.Frame to display treeview in
        :param f_type: Type of data frame requested
        :param index: Index from treeview select
        :param tree_type: Type of data frame requested
        :return: tree for treeview
        '''
        # Display students table based on course selected
        table = None
        if f_type == 's':
            table = self.df_query.get_students_df(course)
        if f_type == 'a':
            if asgn_type == 'ind':
                table = self.df_query.get_assignments_index(course)
            elif asgn_type == 'asgn':
                table = self.df_query.get_assignments_name(course, index)
            elif asgn_type == 'grades':
                table = self.df_query.get_grades(course, index)
        tree = self.display_tree(table, frame)

        return tree

    def display_tree(self, data_table, tree):
        '''
        Display table in treeview widget
        :param data_table:pandas data frame
        :param tree: treeview frame
        :return: treeview for display in widget
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
        string1 = tree.item(cur_item)['values']
        self.index = ''.join(string1)
        if isinstance(self.index, type(0)):
            self.index = int(self.index+1)
        self.cur_item = cur_item
        return self.index

    def chart_plot(self, course, asgn_type, chart_type, index=None):
        self.destroy_child_widgets(self.analysis_page.graph_frame)
        if asgn_type == 'grades':
            data_frame = self.df_query.get_grades(course, index)
            self.analysis_page.plot_line(self.analysis_page.graph_frame, asgn_type, data_frame, chart_type, index)
        elif asgn_type == "asgn":
            data_frame = self.df_query.get_assignments_name(course, index)
            self.analysis_page.plot_line(self.analysis_page.graph_frame, asgn_type, data_frame, chart_type, index)


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

