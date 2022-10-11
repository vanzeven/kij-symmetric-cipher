from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

class DES_CFB:
    def __init__(self, key, iv):
        self.key = pad(key, DES.block_size)
        self.iv = pad(iv, DES.block_size)

    def encrypt(self, plaintext):
        padded_bytes = pad(plaintext, DES.block_size)
        DES_obj = DES.new(self.key, DES.MODE_CFB, self.iv)
        chipertext = DES_obj.encrypt(padded_bytes)
        return chipertext

    def decrypt(self, ciphertext):
        DES_obj = DES.new(self.key, DES.MODE_CFB, self.iv)
        raw_bytes = DES_obj.decrypt(ciphertext)
        extracted_bytes = unpad(raw_bytes, DES.block_size)
        return extracted_bytes  