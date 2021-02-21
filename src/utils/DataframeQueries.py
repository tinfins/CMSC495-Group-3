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

    def get_students(self, course):
        '''
        :param course:
        :param df:pandas dataframe
        :return:dataframe of student name
        '''
        self.df_students = self.df.loc[self.df['course_name'] == course][['student_lname', 'student_fname']]
        return self.df_students

    def get_assignments(self, course, df):
        data_table = self.df.loc[self.df['course_name'] == course][['student_lname', 'student_fname', 'course_name']]
        return data_table


if __name__ == '__main__':
    # Uncomment when query by professor
    dataf = pd.read_csv('data-export.csv', header=0)
    # Uncomment when full data query
    # dataf = pd.read_csv('full-data-export.csv', header=0)
    dframe = DataframeQueries(dataf)
    dframe.student_name(dframe.df)
    print(dframe.df)
    print(dframe.df_students)
