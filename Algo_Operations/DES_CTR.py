from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

class DES_CTR:
    def __init__(self, key, iv):
        self.key = pad(key, DES.block_size)
        self.iv = pad(iv, DES.block_size)
        self.nonce = self.iv
        
    def encrypt(self, plaintext):
        #data_bytes = bytes(plaintext, 'utf-8')
        padded_bytes = pad(plaintext, DES.block_size)
        DES_obj = DES.new(self.key, DES.MODE_CTR)
        chipertext,nonce = DES_obj.encrypt(padded_bytes)
        self.nonce=nonce
        return chipertext

    def decrypt(self, ciphertext):
        DES_obj = DES.new(self.key, DES.MODE_CTR,nonce=self.nonce)
        raw_bytes = DES_obj.decrypt(ciphertext)
        extracted_bytes = unpad(raw_bytes, DES.block_size)
        return extracted_bytes  