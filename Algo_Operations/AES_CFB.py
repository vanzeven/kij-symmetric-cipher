from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

class AES_CFB:
    def __init__(self, key, iv):
        self.key = pad(key, AES.block_size)
        self.iv = pad(iv, AES.block_size)

    def encrypt(self, plaintext):
        padded_bytes = pad(plaintext, AES.block_size)
        AES_obj = AES.new(self.key, AES.MODE_CFB, self.iv)
        chipertext = AES_obj.encrypt(padded_bytes)
        return chipertext

    def decrypt(self, ciphertext):
        AES_obj = AES.new(self.key, AES.MODE_CFB, self.iv)
        raw_bytes = AES_obj.decrypt(ciphertext)
        extracted_bytes = unpad(raw_bytes, AES.block_size)
        return extracted_bytes  