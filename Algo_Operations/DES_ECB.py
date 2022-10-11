from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

class DES_ECB:
    def __init__(self, key, iv = None):
        self.key = pad(key, DES.block_size)
        self.iv = None

    def encrypt(self, plaintext):
        padded_bytes = pad(plaintext, DES.block_size)
        DES_obj = DES.new(self.key, DES.MODE_ECB)
        chipertext = DES_obj.encrypt(padded_bytes)
        return chipertext

    def decrypt(self, ciphertext):
        DES_obj = DES.new(self.key, DES.MODE_ECB)
        raw_bytes = DES_obj.decrypt(ciphertext)
        extracted_bytes = unpad(raw_bytes, DES.block_size)
        return extracted_bytes