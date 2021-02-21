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
import logging.config
import sqlalchemy as db
#import cx_Oracle
#import psycopg2
#import pyodbc
# Big Teacher module imports
from src.model.DataModel import SettingsModel


class Connector:
    '''
    Controller for user credentialing and queries
    '''

    def __init__(self, username, password, config_values):
        '''
        Initializes DB Connector
        :params username:String
        :params password:String
        '''
        self.logger = logging.getLogger(__name__)
        self.settings_model = SettingsModel(_dialect=config_values['db_type'], _username=username,
                                                      _password=password, _host=config_values['host'],
                                                      _port=config_values['port'], _db_name=config_values['db_name'])
        self.engine = None
        self.conn = None

    def create_engine(self, settings_model):
        '''
        :param settings:Obj:Object of sqldb section from config.ini
        :return:engine.object
        '''
        # Dict for different dialect/drivers
        driver_dict = {'mysql': 'pymysql', 'oracle': 'cx_oracle', 'postgresql': 'psycogp2', 'mssql': 'pyodbbc'}
        settings_obj = settings_model
        dialect = None
        driver = None
        for key, value in driver_dict.items():
            if settings_obj.dialect == key:
                dialect = key
                driver = value

        # SQLAlchemy Engine is used to connect to db and perform all queries
        self.engine = db.create_engine(
            f"{dialect}+{driver}://{settings_obj.username}:{settings_obj.password}@{settings_obj.host}:{settings_obj.port}/{settings_obj.db_name}")
        return self.engine

    def login(self, engine):
        '''
        Perform login function
        '''
        try:
            with engine.connect() as self.conn:
                return True
        except (db.exc.OperationalError, RuntimeError):
            return False
