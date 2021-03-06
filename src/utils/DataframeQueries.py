import logging
import pandas as pd


class DataframeQueries:
    '''
    Handle dataframe manipulation and queries
    '''

    def __init__(self):
        '''
        :params data_frame:Pandas dataframe
        '''
        self.logger = logging.getLogger(__name__)
        self.df = None
        self.df_students = None

    def create_dataframe(self, result):
        #self.df = pd.read_csv(result)
        self.df = pd.DataFrame(result)
        self.df.columns = result[0].keys()
        return self.df

    def get_classes(self):
        '''
        DataFrame is already localized to professor based on login
        '''
        classes = self.df['course_name'].unique()
        course_names = []
        for course in classes:
            course_names.append(course)
        return tuple(classes)

    def get_students_df(self, course):
        '''
        :param course:
        :param df:pandas dataframe
        :return:dataframe of student name
        '''
        self.df['Name'] = self.df.student_lname.str.cat(self.df.student_fname, sep=', ')
        self.df_students = self.df.loc[self.df['course_name'] == course][['Name']].copy()
        return self.df_students.sort_values('Name', ascending=False)
    
    def get_assignments(self, course):
        '''
        Sorts dataframe by course
        :param course: Course name for sorting
        :return: dataframe of all assignments and name of selected course
        '''
        self.df['Name'] = self.df.student_lname.str.cat(self.df.student_fname, sep=', ')
        df1 = self.df.loc[self.df['course_name'] == course][['Name', 'course_name', 'homework_1', 'homework_2', 'homework_3', 'homework_4', 'homework_5', 'homework_6', 'homework_7', 'homework_8', 'quiz_1', 'quiz_2', 'quiz_3', 'quiz_4', 'quiz_5', 'quiz_6', 'quiz_7', 'quiz_8', 'test_1', 'test_2', 'test_3', 'test_4', 'test_5', 'test_6', 'test_7', 'test_8']].copy()
        # Rename columns
        for name in df1.columns:
            new_name = name.replace('_', ' ').capitalize()
            df1.rename({name: new_name}, axis=1, inplace=True)
        return df1

    def get_assignments_index(self, course):
        '''
        Returns assignments name only
        :param course: Course name to pass to get_assignments
        :return: data frame of assignments names
        '''
        data_frame = self.get_assignments(course)
        data_frame.pop('Name')
        data_frame.pop('Course name')
        df = pd.DataFrame(data_frame.columns)
        df.columns = ['Assignments']
        return df.sort_values('Assignments', ascending=False)

    def get_assignments_name(self, course, index):
        '''
        Gets name and assignment grads of associated index
        :param course: Course name to pass to get_assignments
        :param index: Index from treeview select for selected assignment
        :return: Data frame of students and assignment grade of selected assignment
        '''
        data_frame = self.get_assignments(course)
        for column in data_frame.columns:
            if column == index:
                df = data_frame[['Name', index]]
                return df.sort_values('Name', ascending=False)

    def get_grades(self, course, index):
        '''
        Return grades from selected student
        :param course: Course value to pass to get_assignments
        :param index: Index of student name
        :return: Data frame of assignments grades of selected student
        '''
        data_frame = self.get_assignments(course)
        data_frame.pop('Course name')
        # Transpose table for cols as index
        df1T = data_frame.set_index('Name').T
        df1T.insert(loc=0, column='Assignments', value=df1T.index)
        df2 = df1T.sort_index(ascending=True).reset_index(level=0, drop=True)
        df2 = df2.loc[:, ['Assignments', index]]
        return df2.sort_index(ascending=False)
