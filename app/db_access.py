# Author: PiereLucas(Julian Huch)
# MIT LICENSE


import sqlite3
import os
import sys
import random
import time
from hashlib import sha256


class Gen_DB():
    """ Class for checking of the given database and username exists """

    def __init__(self, db_name, user):
        self.user_hash = sha256(user.encode("UTF-8")).hexdigest()
        self.connection = self.generate_db(db_name)

    
    def __repr__(self):
        return "%s" % self.__class__.__name__

    def generate_db(self, db_name):
        try:

            if os.path.isfile(db_name):
                connection = sqlite3.connect(db_name)
                cursor = connection.cursor()

                sql = "SELECT * FROM user"
                cursor.execute(sql)
                for data in cursor:
                    if self.user_hash == data[0]:
                        del sql; del cursor
                        print("Sucessfully logged in DB: [%s]" % db_name)
                        return connection
                    else:
                        print("Wrong Username for DB: [%s]" % db_name)
                        sys.exit(1)

            else:
                print("CREATE NEW DB: [%s]" % db_name)

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

                sql = f"CREATE TABLE user(" \
                    f"Username TEXT)"
                cursor.execute(sql)

                sql = f"INSERT INTO user VALUES('{self.user_hash}')"
                cursor.execute(sql)
                connection.commit()

                print("Successfully CREATED DB: [%s]" % db_name)
                del sql; del cursor
                return connection
        except Exception as ex:
            print("Error in %s : %s" % (self.__class__.__name__, ex))
            sys.exit(1)


class DBAccess(Gen_DB):
    """ Write, read and delete entrys in the given database """

    def __init__(self, db_name, user):
        super(DBAccess, self).__init__(db_name, user)

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
                print("Successfully INSERT data INTO Columne: [%s] in DB: [%s]" % (service_name, self.db_name))
                return
        blank_new_entry()
        print("Successfully CREATE and INSERT data INTO Columne: [%s] in DB: [%s]" % (service_name, self.db_name))
        return

    def readdb(self, service_name):
        sql = "SELECT * FROM main"
        self.execute(sql)
        return [data for data in self.cursor if service_name == data[0]]

    def deldb(self, service_name):
        sql = f"DELETE FROM main WHERE(Service='{service_name}')"
        self.execute(sql)
        self.connection.commit()

        print("Sucessfully DELETED Columne: [%s] from DB: [%s]" % (service_name, self.db_name))
        return

    def close(self):
        self.connection.close()


if __name__ == "__main__":
    """ This is just for debugging """

    dba = DBAccess("passmandb", "Peter")
    dba.writedb("google.de", "peter@aol.com", "s3cr3tpass", "Thats my first account")
    #dba.deldb("google.de")
    for i, data in enumerate(dba.readdb("google.de"), start=1):
        print("[%d] Service: %s  Login: %s   Password: %s    Created: %s     Modified: %s    Note: %s" 
            % (i, data[0], data[1], data[2], data[3], data[4], data[5]))
    dba.close()
