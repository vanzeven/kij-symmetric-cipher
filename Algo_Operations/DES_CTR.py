import os

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Util import Counter

class DES_CTR:
    def __init__(self, key, iv):
        self.key = pad(key, DES.block_size)
        self.iv = None
        self.ctr = iv[:4]

        self.counter = Counter.new(32, self.ctr)
        
    def encrypt(self, plaintext):
        padded_bytes = pad(plaintext, DES.block_size)
        DES_obj = DES.new(self.key, DES.MODE_CTR, counter=self.counter)
        chipertext = DES_obj.encrypt(padded_bytes)
        return chipertext

    def decrypt(self, ciphertext):
        DES_obj = DES.new(self.key, DES.MODE_CTR, counter=self.counter)
        raw_bytes = DES_obj.decrypt(ciphertext)
        extracted_bytes = unpad(raw_bytes, DES.block_size)
        return extracted_bytes  