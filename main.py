# Author: PiereLucas(Julian Huch)
# MIT LICENSE


import time
from getpass import getpass
from app import *


from colorama import Fore, Style
Green = Fore.GREEN
Red = Fore.RED
Reset = Style.RESET_ALL


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
        self.db_name = input("DB Name [passmandb] > ")
        self.cryptkey = getpass("Manager Password > ")

        if choice == 1:
            self.service_name, self.login, password, self.note = input("Service, Login, Password, Note > ").split(",")
            aes = cryptmodule.AES_ECB(self.cryptkey)
            self.password = aes.enc(password)
            
            dba = db_access.DBAccess(db_name=self.db_name if self.db_name != "" else "passmandb")
            dba.writedb(self.service_name, self.login, self.password, self.note)
            dba.close()

        elif choice == 2:
            self.service_name = input("Service > ")
            dba = db_access.DBAccess(db_name=self.db_name if self.db_name != "" else "passmandb")
            aes = cryptmodule.AES_ECB(self.cryptkey)
            for i, data in enumerate(dba.readdb(self.service_name), start=1):
                print("-----[%d]-----\nService: %s\nLogin: %s\nPassword: %s\nService Created: %s\nModified: %s\nNote: %s" 
                    % (i, data[0], data[1], aes.dec(data[2]), data[3], data[4], data[5]))
            dba.close()
            
        elif choice == 3:
            self.service_name = input("Service > ")
            dba = db_access.DBAccess(db_name=self.db_name if self.db_name != "" else "passmandb")
            dba.deldb(self.service_name)
            dba.close()

    def run(self):
        self.infunc()      


if __name__ == "__main__":
    rc = RunClass()
    rc.run()
