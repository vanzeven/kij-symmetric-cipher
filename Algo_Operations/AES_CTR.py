import os

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Util import Counter

class AES_CTR:
    def __init__(self, key, iv):
        sum_ctr = 0
        for i in iv:
            sum_ctr += i

        self.key = pad(key, AES.block_size)
        self.iv = None
        self.ctr = sum_ctr

        self.counter = Counter.new(128, initial_value=self.ctr)
        
    def encrypt(self, plaintext):
        padded_bytes = pad(plaintext, AES.block_size)
        AES_obj = AES.new(self.key, AES.MODE_CTR, counter=self.counter)
        chipertext = AES_obj.encrypt(padded_bytes)
        return chipertext

    def decrypt(self, ciphertext):
        AES_obj = AES.new(self.key, AES.MODE_CTR, counter=self.counter)
        raw_bytes = AES_obj.decrypt(ciphertext)
        extracted_bytes = unpad(raw_bytes, AES.block_size)
        return extracted_bytes  