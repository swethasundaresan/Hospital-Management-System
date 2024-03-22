import pyodbc

import util


class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        try:
            if DBConnection.connection is None:
                connection_string = util.PropertyUtil.getPropertyString()
                DBConnection.connection = pyodbc.connect(connection_string)
                print("Database connection successful")
            return DBConnection.connection
        except pyodbc.Error as e:
            print(f"Error connecting to database: {e}")
            raise
