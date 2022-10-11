from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

class DES_OFB:
    def __init__(self, key, iv):
        self.key = pad(key, DES.block_size)
        self.iv = pad(iv, DES.block_size)

    def encrypt(self, plaintext):
       # data_bytes = bytes(plaintext, 'utf-8')
        padded_bytes = pad(plaintext, DES.block_size)
        DES_obj = DES.new(self.key, DES.MODE_OFB, self.iv)
        chipertext = DES_obj.encrypt(padded_bytes)
        return chipertext

    def decrypt(self, ciphertext):
        DES_obj = DES.new(self.key, DES.MODE_OFB, self.iv)
        raw_bytes = DES_obj.decrypt(ciphertext)
        extracted_bytes = unpad(raw_bytes, DES.block_size)
        return extracted_bytes
        