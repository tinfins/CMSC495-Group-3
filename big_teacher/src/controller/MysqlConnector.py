###############################################
# Purpose: Creates connection to mySql        #
# database, performs queries, and login and   #
# logout functions.                           #
#                                             #
# Licensed under the MIT license. See LICENSE #
# file in project root for details.           #
#                                             #
# https://github.com/tinfins/CMSC495-Group-3/ #
###############################################

import sys
import logging.config
import sqlalchemy as db
from sqlalchemy.sql import text
#import cx_Oracle
#import psycopg2
#import pyodbc
import pandas as pd
import big_teacher.src.model.DataModel as DataModel


class MysqlConnector:
    '''
    Create MySQL DB connection. Execute MySQL statements
    '''
    @classmethod
    def create_engine(cls, settings):
        '''
        :param settings:Obj:Object of sqldb section from config.ini
        '''
        cls.logger = logging.getLogger(__name__)
        # Dict for different dialect/drivers
        driver_dict = {'mysql': 'pymysql', 'oracle': 'cx_oracle', 'postgresql': 'psycogp2', 'mssql': 'pyodbbc'}
        settings_obj = settings
        dialect = None
        driver = None
        for key, value in driver_dict.items():
            if settings_obj.dialect == key:
                dialect = key
                driver = value

        # SQLAlchemy Engine is used to connect to db and perform all queries
        cls.engine = db.create_engine(f"{dialect}+{driver}://{settings_obj.username}:{settings_obj.password}@{settings_obj.host}:{settings_obj.port}/{settings_obj.db_name}")
        return cls.engine

    @classmethod
    def login(cls, engine, settings):
        '''
        Login method, also tests connection to database
        :param engine:Obj:engine object from sqlalchemy
        :param settings:Obj:settings object
        :return:prof_obj:If connection successful, returns prof_obj professor info
        Closes db connection after connection. Engine stays active
        '''
        try:
            username = settings.username[1:].capitalize()
            conn = engine.connect()
            sql_query = text('SELECT * FROM professors WHERE last_name = :x')
            result = conn.execute(sql_query, x=username).fetchall()
            prof_obj = DataModel.ProfessorModel(prof_id=result[0]['professor_id'], prof_fname=result[0]['first_name'], prof_lname=result[0]['last_name'], prof_email=result[0]['email'])
            cls.logger.info(f"Successful login - {settings.username}")
            return prof_obj
        except:
            logging.critical(f"FAILED login - {settings.username}")

    
    @classmethod
    def get_data(cls, engine, prof):
        '''
        Get data method, retrieves data from database and returns pandas dataframe
        :param engine:Obj:engine object from sqlalchemy
        :param prof:Obj:professor model
        :return:df:If successful, returns matching data from db as dataframe
        Closes db connection after connection. Engine stays active
        '''
        prof_lname = prof.prof_lname
        try:
            conn = engine.connect()
            sql_query = text('SELECT * FROM StudentView WHERE prof_last_name = :x')
            result = conn.execute(sql_query, x=prof_lname).fetchall()
            df = pd.DataFrame(result)
            df.columns = result[0].keys()
            cls.logger.info('Data successfully retrieved')
            return df
        except:
            cls.logger.error('Unable to fetch data...quitting...')
            sys.exit(0)


    @classmethod
    def logout(cls):
        '''
        Logout method, disposes of engine and connection pool
        :return:False
        '''
        cls.engine.dispose()
        return False