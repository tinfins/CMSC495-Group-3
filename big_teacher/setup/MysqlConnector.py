##########################
# Purpose: Executes multiple SQL  #
# statements in Python with            #
# mysql.connector.                            #
#                                                            #
# Licensed under the MIT license.  #
# See LICENSE file in project root   #
# for details.                                        #
#                                                            #
# https://github.com/tinfins/           #
# CMSC495-Group-3/                        #
##########################

import mysql.connector

class MysqlConnector():
    
    mydb = mysql.connector.connect(
    host="cmsc495.cnqrtayefs7j.us-east-2.rds.amazonaws.com",
    user="admin_cmsc495",
    password="CMSC495CMSC$(%",
    database="cmsc495"
)
    @classmethod
    def multiple_statements(self, conn, statements, rollback_on_error=True):
        """
        Execute creation of multiple mysql statements and returns cursor from the last executed statement

        :param Conn: The connection to the database
        :type Conn: Database connection

        :param statements: The statements to be executed
        :type statements: A list of strings
    
        : param rollback_on_error: Flag to indicate action to be taken on an exception
        :type rollback_on_error: book

        :return: cursor from the last statement executed
        :rtype cursor
        """
    
        try:
            cursor = conn.cursor()
            for statement in statements:
                cursor.execute(statement)
                if not rollback_on_error:
                    conn.commit()
        except Exception as e:
            if rollback_on_error:
                conn.rollback()
            raise
        # commit only after all statements have completed successfully
        else:
            if rollback_on_error:
                conn.commit()
            return cursor
    