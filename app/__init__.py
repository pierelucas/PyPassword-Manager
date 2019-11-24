from app import crypt


# Globals
encoding_std = "UTF-8"


class App():

    def __init__(self, db_name, service_name, personal_key):
        self.aes_ecb = crypt.AES_ECB(personal_key)
