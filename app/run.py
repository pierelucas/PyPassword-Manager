# Author: PiereLucas(Julian Huch)
# MIT LICENSE


import time
from getpass import getpass
import crypt
import db_access


class RunClass():

    def __init__(self):
        
        self.lt = time.localtime()

        self.author = "Julian Huch"
        self.license = "MIT LICENSE"
        self.version = "1.0"
        
        self.banner_txt = """
        ---------------------
        PyPassword - Manager
        Coding by %s
            Version: %s
                %s
        ---------------------
        """ % (self.author, self.version, self.license)

        self.menu_txt = """
        [1] Write entry to DB
        [2] Read entry's
        [3] Delete entry's

        Please insert Database name (Default: passmandb)
        """

        self.cryptkey = ""

        self.service_name = ""
        self.db_name = ""
        self.login = ""
        self.password = ""
        self.note = ""

    def __repr__(self):
        return "%s" % self.__class__.__name__
    
    def infunc(self):
        print("%s\n%s" % (self.banner_txt, self.menu_txt))
        choice = int(input("Choice > "))
        self.db_name = input("DB Name > ")
        self.cryptkey = getpass("Manager Password > ")
        if choice == 1:
            self.service_name, self.login, self.password, self.note = input("Service, Login, Password, Note > ").split()
            pass
        elif choice == 2:
            self.service_name = input("Service > ")
            pass
        elif choice == 3:
            self.service_name = input("Service > ")
            pass

    def outfunc(self):
        pass

    def run(self):
        pass
        

def main():
    rc = RunClass()
    rc.run()