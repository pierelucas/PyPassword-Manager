import sqlite3
import os
import sys
import random
import time


class Gen_DB():

    def __init__(self, db_name):
        self.connection = self.generate_db(db_name)

    def generate_db(self, db_name):
        try:
            if os.path.isfile(db_name):
                return sqlite3.connect(db_name)
            else:
                print("Generate new Database: %s" % db_name)
                connection = sqlite3.connect(db_name)
                cursor = connection.cursor()
                sql = "CREATE TABLE main("  \
                    "Service TEXT, " \
                    "Password TEXT, " \
                    "Created TEXT, " \
                    "LastMod TEXT)"
                cursor.execute(sql)
                print("%s \n Successfully generated Database: %s" % (sql, db_name))
                del sql; del cursor
                return connection
        except Exception as ex:
            print("Error in %s : %s" % (self.__class__.__name__, ex))
            sys.exit(1)


class DBAccess(Gen_DB):

    def __init__(self, db_name="passmandb"):
        super(DBAccess, self).__init__(db_name)

        self.date_today = time.strftime("%d.%m.%Y", time.localtime())

        self.db_name = db_name
        self.cursor = self.connection.cursor()
        self.execute = lambda var: self.cursor.execute(var)
    
    def writedb(self, service_name, password):
        sql = ""
        self.execute(sql)

    def readdb(self, service_name):
        sql = "SELECT * FROM main"
        self.execute(sql)
        for data in self.cursor:
            if service_name in data[0]:
                return data[0], data[1], data[2], data[3]
            else:
                return "Service Name not found in DB: %s" % self.db_name

    def moddb(self, service_name, password):
        sql = ""
        self.execute(sql)

    def deldb(self, service_name):
        sql = ""
        self.execute(sql)


if __name__ == "__main__":
    pass
