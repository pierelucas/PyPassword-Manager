# Author: PiereLucas(Julian Huch)
# MIT LICENSE


""" 
This is just a small and thin wrapper around the zxcvbn (password scoring) library from dropbox.
It gives you in return a dictionary with some infos about your given password.
usage: scoring = password_scoring.Scoring(password)
       results = scoring()
"""


from zxcvbn import zxcvbn as passcheck


class Scoring():
    """ Callable Scoring Class """


    def __init__(self, password):
        self.user_password = password
        self.cret = dict()

    def __repr__(self):
        return "%s" % self.__class__.__name__
    
    def __call__(self):
        d = passcheck(self.user_password)

        result = {
            "Password" : self.user_password,
            "Score" : d["score"],
            "CrackingTime" : d["crack_times_display"]["offline_slow_hashing_1e4_per_second"],    # offline_fast_hashing_1e10_per_second
            "Suggestions" : d["feedback"]["suggestions"] 
        }

        for key, value in result.items():
            
            """
            Instead the block below you can use this short comprehension and 
            pythonic solution when u didnt neeed the "Everything is Fine" sentence.
            print(f"{key:<15}: {' '.join(value) if isinstance(value, list) else value}")
            """

            if isinstance(value, list):
                value = " ".join(value if value != [] else ["Everything is Fine"])
            self.cret[key] = value
        
        return self.cret


if __name__ == "__main__":
    """ This is just for debugging """

    sc = Scoring(input("Password > "))
    d = sc()
    print("\n".join([f"{key:<15}:{value}" for key, value in d.items()]))
