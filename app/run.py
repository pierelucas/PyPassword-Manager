# Author: PiereLucas(Julian Huch)
# MIT LICENSE


from app import *


class RunClass():

    def __repr__(self):
        return "%s" % self.__class__.__name__
    
    def infunc(self):
        pass

    def outfunc(self):
        pass

    def run(self):
        pass



rc = RunClass()
rc.run()