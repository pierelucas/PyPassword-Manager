# Author: PiereLucas(Julian Huch)
# MIT LICENSE


from base64 import b64encode, b64decode
from Crypto.Cipher import AES
import hashlib
import app


class Hasher():

    def __init__(self, raw_key):
        self.encoding_ = app.encoding_std
        self.key = self.hashit(raw_key)
        

    def hashit(self, key) -> bytes:
        return hashlib.sha256(str(key).encode(self.encoding_))


class AES_ECB(Hasher):

    def __init__(self, raw_key):
        super(AES_ECB, self).__init__(raw_key)
        self.aes = AES.new(self.key.digest(), AES.MODE_ECB)

    def make_len(self, string) -> bytes:
        bytestring = string.encode(self.encoding_)
        while len(bytestring) < 16:
            bytestring += b"\x00"
        return bytestring

    def enc(self, string) -> str:
        bytestring = self.make_len(string)
        hx_enc = self.aes.encrypt(bytestring)
        return b64encode(hx_enc).decode(self.encoding_)

    def dec(self, cipher) -> str:
        tmp_cip = b64decode(cipher.encode(self.encoding_))
        hx_dec = self.aes.decrypt(tmp_cip)
        return hx_dec.decode(self.encoding_)


if __name__ == "__main__":

    string_to_encrypt = str(input("Raw String > "))
    key = input("Encryption Key > ")

    object = AES_ECB(key)
    encrypted_cipher = object.enc(string_to_encrypt)
    decrypted_string =  object.dec(encrypted_cipher)

    print("Encrypted >", encrypted_cipher)
    print("Decrypted >", decrypted_string)
