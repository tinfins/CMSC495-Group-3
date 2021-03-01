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

    def get_students_df(self, course):
        '''
        :param course:
        :param df:pandas dataframe
        :return:dataframe of student name
        '''
        self.df['Name'] = self.df.student_lname.str.cat(self.df.student_fname, sep=', ')
        self.df_students = self.df.loc[self.df['course_name'] == course][['Name']]
        return self.df_students

    def get_assignments(self, index=None, tree_type=None, course=None):
        # Combine last_name, first_name to Name
        self.df['Name'] = self.df.student_lname.str.cat(self.df.student_fname, sep=', ')
        # Fine total amount of columns in df
        length = len(self.df.columns)
        # Slice df to keep col 9 and up
        df1 = self.df.iloc[:, 9:length].copy()
        # Rename columns
        for name in df1.columns:
            new_name = name.replace('_', ' ').capitalize()
            df1.rename({name: new_name}, axis=1, inplace=True)
            # Transpose table for cols as index
        df1T = df1.set_index('Name').T
        df1T.insert(loc=0, column='Assignments', value=df1T.index)
        df2 = df1T.sort_index(ascending=True).reset_index(level=0, drop=True)
        if isinstance(index, type(0)):
            df2 = df2.iloc[:, [0, index]]
            return df2.sort_index(ascending=True)
        elif tree_type == 'asgn':
            df2 = df2.iloc[:, 0:length]
            return df2.sort_index(ascending=True)
        elif tree_type == 'ind':
            df2 = df2.iloc[:, 0:1]
            return df2.sort_index(ascending=True)
        elif index is None and tree_type is None:
            df2 = pd.DataFrame()
            return df2.sort_index(ascending=True)

    def assignments_index(self, dfT, index=None):
        if isinstance(index, type(0)):
            df2 = dfT.iloc[:, [0, index]]
        else:
            length = len(dfT.columns)
            df2 = dfT.iloc[:, 0:length]
        return df2

'''
    def try_assignments(self, index=None):
        # Fine total amount of columns in df
        length = len(self.df.columns)
        # Slice df to keep col 9 and up
        df1 = self.df.iloc[:, 9:length].copy()
        # Rename columns
        for name in df1.columns:
            new_name = name.replace('_', ' ').capitalize()
            df1.rename({name: new_name}, axis=1, inplace=True)
            # Transpose table for cols as index
'''
