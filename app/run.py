# Author: PiereLucas(Julian Huch)
# MIT LICENSE


import time
from app import *


class RunClass():

    def __init__(self):
        
        self.lt = time.localtime()
        
        self.author = "Julian Huch"
        self.license = "MIT LICENSE"
        self.version = "1.0"
        
        banner_txt = """
        ---------------------
        PyPassword - Manager
        Coding by %s
            Version: %s
                %s
        ---------------------
        """ % (self.author, self.version, self.license)

        menu_txt = """
        [1] Write entry to DB
        [2] Read entry's
        [3] Delete entry's
        """

    def __repr__(self):
        return "%s" % self.__class__.__name__
    
    def infunc(self):
        pass

    def outfunc(self):
        pass

    def run(self):
        



rc = RunClass()
rc.run()