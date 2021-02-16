import logging.config
# Big Teacher module imports
import big_teacher.src.gui.AssignmentsPage as AssignmentsPage


class AssignmentsPageController:
    '''
    AssignmentsPage controller for application
    '''

    def __init__(self, master, controller, layout, content_frame, engine, prof, data_frame):
        '''
        Initializes AssignmentsPageController and displays AssignmentsPage gui
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
        self.assignments_page = AssignmentsPage.AssignmentsPage(self.master, self.controller, self.content_frame)
        self.assignments_page.tkraise()
        self.engine = engine
        self.prof = prof
        self.data_frame = data_frame

        self.controller.main_view.home_button.config(command=lambda: (self.controller.destroy_child_widgets(), self.controller.home_frame()))

        # Dynamically set course combobox
        self.assignments_page.class_subject['values'] = self.get_classes()
        self.assignments_page.class_subject.current(0)

    def get_classes(self):
        '''
        DataFrame is already localized to professor based on login
        '''
        classes = self.data_frame['course_name'].unique()
        course_names = []
        for course in classes:
            course_names.append(course)
        return tuple(classes)
