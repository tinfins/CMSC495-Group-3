import logging
import sqlalchemy as db
from sqlalchemy.sql import text
import pandas as pd
# Big Teacher module imports
from src.model.DataModel import ProfessorModel


class DatabaseQuery:
    '''
    Performs database and dataframe queries
    '''

    def __init__(self, engine):
        '''
        :params engine:sqlalchemy.engine()
        :return:Professor model object
        '''
        self.logger = logging.getLogger(__name__)
        self.engine = engine
        self.prof_obj = None
        self.df = None
        # Table Details
        self.students = None
        self.student_to_course = None
        self.professors = None
        self.teacher_to_course = None
        self.courses = None
        self.tests = None

    def get_prof(self, settings):
        '''
        Query database for professor information
        '''
        try:
            username = settings.username[1:].capitalize()
            sql_query = text('SELECT * FROM professors WHERE last_name = :x')
            with self.engine.connect() as conn:
                result = conn.execute(sql_query, x=username).fetchall()
            # result = connection.execute(sql_query, x=username).fetchall()
            self.prof_obj = ProfessorModel(prof_id=result[0]['professor_id'],
                                                     prof_fname=result[0]['first_name'],
                                                     prof_lname=result[0]['last_name'], prof_email=result[0]['email'])
            return self.prof_obj
        except:
            self.logger.error('Can not retrieve professor information')
            return None

    def get_tables(self):
        '''
        Retrieves remote Table schema and metadata
        '''
        metadata = db.MetaData()
        with self.engine.connect() as conn:
            self.students = db.Table('students', metadata, autoload=True, autoload_with=self.engine)
            self.student_to_course = db.Table('student_to_course', metadata, autoload=True, autoload_with=self.engine)
            self.professors = db.Table('professors', metadata, autoload=True, autoload_with=self.engine)
            self.teacher_to_course = db.Table('teacher_to_course', metadata, autoload=True, autoload_with=self.engine)
            self.courses = db.Table('courses', metadata, autoload=True, autoload_with=self.engine)
            self.tests = db.Table('tests', metadata, autoload=True, autoload_with=self.engine)

    def get_data(self, prof):
        '''
        :params prof:Professor data object
        :return:Pandas data frame
        '''
        prof_lname = prof.prof_lname
        self.get_tables()
        s = self.students  # students table
        stc = self.student_to_course  # student_to_course table
        p = self.professors  # professors table
        ttc = self.teacher_to_course  # teacher_to_course table
        c = self.courses  # course table
        t = self.tests  # tests table
        # Column select from joined tables
        sel = db.select([s.c.first_name.label('student_fname'), s.c.last_name.label('student_lname'),
                         p.c.first_name.label('prof_fname'), p.c.last_name.label('prof_lname'),
                         p.c.email.label('prof_email'), c.c.name.label('course_name'), c.c.start_date, c.c.end_date,
                         t]).where(p.c.last_name == prof_lname)
        # Join tables and select
        student_course = sel.select_from(
            s.join(stc, s.c.student_id == stc.c.student_id).join(c, stc.c.course_id == c.c.course_id).join(ttc,
                                                                                                           c.c.course_id == ttc.c.course_id).join(
                p, ttc.c.professor_id == p.c.professor_id).join(t, stc.c.student_takes_id == t.c.student_takes_id))
        with self.engine.connect() as conn:
            result = conn.execute(student_course).fetchall()
        self.logger.info('Data successfully retrieved')
        return result
