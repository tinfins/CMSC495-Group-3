####################################
# Purpose: Executes multiple SQL   #
# statements in Python with        #
# mysql.connector.                 #
#                                  #
# Licensed under the MIT license.  #
# See LICENSE file in project root #
# for details.                     #
#                                  #
# https://github.com/tinfins/      #
# CMSC495-Group-3/                 #
####################################

import sys
import MySQLdb as mdb

class MysqlDB():
    """
        Create MySQL DB connection. Execute MySQL statements
    :param host:String:hostname or endpoint
    :param user:String:username for DB
    :param pw:String:password for user
    :param db:String:db name
    """
    
    def __init__(self, host, user, pw, db):
        try:
            self.conn = mdb.connect(host, user, pw, db)
            self.cursor = self.conn.cursor()
        except mdb.Error as e:
            print(f"Error {e.args[0]}: {e.args[1]}" )
            sys.exit(1)
    
    def show_version(self):
        """
        Shows version of database currently connected to
        :return:String:DB version
        """ 
        return self.cursor.execute("SELECT VERSION()")
        
