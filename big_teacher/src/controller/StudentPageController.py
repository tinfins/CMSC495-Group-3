import logging.config
from pandastable import Table, config
# Big Teacher module imports
import big_teacher.src.gui.StudentPage as StudentPage
import pandas as pd


class StudentPageController:
    '''
    StudentPage controller for application
    '''

    def __init__(self, master, controller, layout, content_frame, engine, prof, data_frame):
        '''
        Initializes StudentPageController and displays StudentPage gui
        :params master:tk.Tk():master window
        :params controller:tk.obj:common controller for all views (MainApplication)
        :params layout:tk.Frame:MainLayout frame
        :params content_frame:tk.Frame:frame for sub-page to be displayed in
        :params engine:sql.engine:engine created during login
        :params settings:Obj:settings model
        :params prof:Obj:professor model
        :params data_frame:pandas dataframe:df of db related data
        '''
        self.logger = logging.getLogger(__name__)
        self.master = master
        self.controller = controller
        self.layout = layout
        self.content_frame = content_frame
        self.student_page = StudentPage.StudentPage(self.master, self.controller, self.content_frame)
        self.engine = engine
        self.prof = prof
        self.data_frame = data_frame

        self.controller.main_view.home_button.config(command=lambda: (self.controller.destroy_child_widgets(), self.controller.home_frame()))

        # Dynamically set course combobox
        self.student_page.class_subject['values'] = self.get_classes()
        self.student_page.class_subject.current(0)
        
        self.display_table(self.student_page.class_subject.get())
        
        self.student_page.class_subject.bind('<<ComboboxSelected>>', lambda event: self.display_table(self.student_page.class_subject.get()))
        

    def get_classes(self):
        '''
        DataFrame is already localized to professor based on login
        '''
        classes = self.data_frame['course_name'].unique()
        course_names = []
        for course in classes:
            course_names.append(course)
        return tuple(classes)

    def display_table(self, course):
        data_table = self.data_frame.loc[self.data_frame['course_name'] == course][['student_last_name', 'student_first_name', 'course_name', 'homework_1', 'test_1']]
        print(data_table)
        
        #df = TableModel.getSampleData()
        pt = Table(self.student_page.mid_frame, dataframe=data_table, showtoolbar=True, width=800, height=600)
        options = {'fontsize': 5}
        config.apply_options(options, pt)
        pt.show()
