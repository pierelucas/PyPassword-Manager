# Author: PiereLucas(Julian Huch)
# MIT LICENSE


import sqlite3
import os
import sys
import random
import time


from colorama import Fore, Style
Green = Fore.GREEN
Red = Fore.RED
Reset = Style.RESET_ALL


class Gen_DB():

    def __init__(self, db_name):
        self.connection = self.generate_db(db_name)
    
    def __repr__(self):
        return "%s" % self.__class__.__name__

    def generate_db(self, db_name):
        try:
            if os.path.isfile(db_name):
                return sqlite3.connect(db_name)
            else:
                print(Green + "Generate new Database: %s" + Reset % db_name)
                connection = sqlite3.connect(db_name)
                cursor = connection.cursor()
                sql = f"CREATE TABLE main("  \
                    f"Service TEXT, " \
                    f"Login TEXT, " \
                    f"Password TEXT, " \
                    f"Created TEXT, " \
                    f"LastMod TEXT, " \
                    f"Note TEXT)"
                cursor.execute(sql)
                print(Green + "Successfully generated Database: %s" + Reset % db_name)
                del sql; del cursor
                return connection
        except Exception as ex:
            print(Red + "Error in %s : %s" + Reset % (self.__class__.__name__, ex))
            sys.exit(1)


class DBAccess(Gen_DB):

    def __init__(self, db_name):
        super(DBAccess, self).__init__(db_name)

        self.date_today = time.strftime("%d.%m.%Y - %H:%M", time.localtime())

        self.db_name = db_name
        self.cursor = self.connection.cursor()
        self.execute = lambda var: self.cursor.execute(var)
    
    def __repr__(self):
        return "%s" % self.__class__.__name__

    def writedb(self, service_name, login_name, password, note):
 
        def new_entry(old_date):
            sql = f"INSERT INTO main VALUES('{service_name}', " \
                f"'{login_name}', '{password}', '{old_date}', '{self.date_today}', '{note}')"
            self.execute(sql)
            self.connection.commit()

        def blank_new_entry():
            sql = f"INSERT INTO main VALUES('{service_name}', " \
                f"'{login_name}', '{password}', '{self.date_today}', '{self.date_today}', '{note}')"
            self.execute(sql)
            self.connection.commit()

        sql = "SELECT * FROM main"
        self.execute(sql)
        for data in self.cursor:
            if service_name == data[0]:
                new_entry(old_date=data[3])
                return
        blank_new_entry()
        return

    def readdb(self, service_name):
        sql = "SELECT * FROM main"
        self.execute(sql)
        return [data for data in self.cursor if service_name == data[0]]

    def deldb(self, service_name):
        sql = f"DELETE FROM main WHERE(Service='{service_name}')"
        self.execute(sql)
        self.connection.commit()
        return

    def close(self):
        self.connection.close()


if __name__ == "__main__":
    dba = DBAccess("passmandb")
    dba.writedb("google.de", "123", "345", "Thats my first account")
    #dba.deldb("google.de")
    for i, data in enumerate(dba.readdb("google.de"), start=1):
        print("[%d] Service: %s  Login: %s   Password: %s    Created: %s     Modified: %s    Note: %s" 
            % (i, data[0], data[1], data[2], data[3], data[4], data[5]))
    dba.close()
