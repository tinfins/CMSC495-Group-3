import logging.config
import big_teacher.src.gui.StudentPage as StudentPage


class StudentViewController:
    '''
    HomePage controller for application
    '''
    def __init__(self, master, controller, layout, engine, prof):
        self.logger = logging.getLogger(__name__)
        self.master = master
        self.controller = controller
        self.layout = layout
        self.student_page = StudentPage.StudentPage(self.master, self.controller)
        self.student_page.tkraise()
        self.engine = engine
        self.prof = prof
