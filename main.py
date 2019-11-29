# Author: PiereLucas(Julian Huch)
# MIT LICENSE


from app import *


class RunClass():
    """ Runclass for handling all in and out streams """

    def __init__(self):


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
        [3] Read whole DB
        [4] Delete entry's


                    INFO:
        Default database name: passmandb.
        Your username is your encryption key.
        """

        self.cryptkey = ""

        self.service_name = ""
        self.db_name = ""
        self.login = ""
        self.password = ""
        self.note = ""

        self.scoring = lambda user: password_scoring.Scoring(user)

    def __repr__(self):
        return "%s" % self.__class__.__name__
    
    def infunc(self):
        print("%s\n%s" % (self.banner_txt, self.menu_txt))
        choice = int(input("Choice > "))
        self.db_name = input("DB Name [passmandb] > ")
        self.username = input("Username > ")

        scoring = self.scoring(self.username)
        print("\n" + "\n".join([f"{key:<15}:{value}" for key, value in scoring().items()]) + "\n")

        if choice == 1:
            dba = db_access.DBAccess(db_name=self.db_name if self.db_name != "" else "passmandb", user=self.username)

            self.service_name = input("Service > ")
            aes = cryptmodule.AES_ECB(self.username)
            self.login, self.password, self.note = [aes.enc(i) for i in list(input("Login, Password, Note > ").split(", "))]
            
            dba.writedb(self.service_name, self.login, self.password, self.note)

            dba.close()

        elif choice == 2:
            dba = db_access.DBAccess(db_name=self.db_name if self.db_name != "" else "passmandb", user=self.username)

            self.service_name = input("Service > ")
            aes = cryptmodule.AES_ECB(self.username)

            for i, data in enumerate(dba.read_columne(self.service_name), start=1):
                print("-----[%d]-----\nService: %s\nLogin: %s\nPassword: %s\nService Created: %s\nEntry Created: %s\nNote: %s" 
                    % (i, data[0], aes.dec(data[1]), aes.dec(data[2]), data[3], data[4], aes.dec(data[5])))
            
            dba.close()

        elif choice == 3:
            dba = db_access.DBAccess(db_name=self.db_name if self.db_name != "" else "passmandb", user=self.username)

            aes = cryptmodule.AES_ECB(self.username)

            for i, data in enumerate(dba.read_db(), start=1):
                print("-----[%d]-----\nService: %s\nLogin: %s\nPassword: %s\nService Created: %s\nEntry Created: %s\nNote: %s" 
                    % (i, data[0], aes.dec(data[1]), aes.dec(data[2]), data[3], data[4], aes.dec(data[5])))
            
            dba.close()
            
        elif choice == 4:
            dba = db_access.DBAccess(db_name=self.db_name if self.db_name != "" else "passmandb", user=self.username)
            
            self.service_name = input("Service > ")
            dba.deldb(self.service_name)

            dba.close()

    def run(self):
        self.infunc()      


if __name__ == "__main__":
    """ Run the Programm ! """

    rc = RunClass()
    rc.run()
