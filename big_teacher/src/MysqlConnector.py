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
import logging

logger = logging.getLogger(__name__)


class MysqlConnector:
    '''
    Create MySQL DB connection. Execute MySQL statements
    '''
    def __init__(self, config_dict):
        '''
        :param config_dict:Dict:Dictionary of mysql_db section from config.ini
        '''
        self.config_dict = config_dict
        self.engine = db.create_engine(f"mysql+pymysql://{self.config_dict['username']}:{self.config_dict['password']}@{self.config_dict['host']}:{self.config_dict['port']}/{self.config_dict['db_name']}")
        self.username = self.config_dict['username']

    def login(self):
        '''
        Login method, also tests connection to database
        :return:True:If connection successful, returns True
        Closes db connection after connection. Engine stays active
        '''
        try:
            self.engine.connect()
            logging.info(f"Successful login - {self.config_dict['username']}")
            return True
        except:
            logging.critical(f"FAILED login - {self.config_dict['username']}")

    def logout(self):
        '''
        Logout method, disposes of engine and closes connection
        :return:String
        '''
        self.engine.dispose()
        #TODO:
        return self.config_dict['username']
