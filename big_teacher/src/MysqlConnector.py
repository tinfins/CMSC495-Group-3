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

import sqlalchemy as db
import pymysql
import cx_Oracle
import psycopg2
import pyodbc
import logging
import big_teacher.src.model.DataModel as DataModel

logger = logging.getLogger(__name__)


class MysqlConnector:
    '''
    Create MySQL DB connection. Execute MySQL statements
    '''
    def __init__(self, settings):
        '''
        :param config_dict:Dict:Dictionary of mysql_db section from config.ini
        '''
        # Dict for different dialect/drivers
        driver_dict = {'mysql': 'pymysql', 'oracle': 'cx_oracle', 'postgresql': 'psycogp2', 'mssql': 'pyodbbc'}
        self.settings_obj = settings
        self.dialect = None
        self.driver = None
        for key, value in driver_dict.items():
            if self.settings_obj.dialect == key:
                self.dialect = key
                self.driver = value

        self.engine = db.create_engine(f"{self.dialect}+{self.driver}://{self.settings_obj.username}:{self.settings_obj.password}@{self.settings_obj.host}:{self.settings_obj.port}/{self.settings_obj.db_name}")

    def login(self):
        '''
        Login method, also tests connection to database
        :return:True:If connection successful, returns True
        Closes db connection after connection. Engine stays active
        '''
        try:
            self.engine.connect()
            logging.info(f"Successful login - {self.settings_obj.username}")
            return True
        except:
            logging.critical(f"FAILED login - {self.settings_obj.username}")

    def logout(self):
        '''
        Logout method, disposes of engine and closes connection
        :return:String
        '''
        self.engine.dispose()
        #TODO:
        return self.settings_obj.username
