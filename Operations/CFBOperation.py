from Operations.Operation import Operation
from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

class CFBOperation(Operation):
    def __init__(self):
        pass

    def encrypt(self, algorithmClass, plaintext, key, iv):
        data_bytes = bytes(plaintext, 'utf-8')
        padded_bytes = pad(data_bytes, AES.block_size)
        AES_obj = AES.new(key, AES.MODE_CFB, iv)
        chipertext = AES_obj.encrypt(padded_bytes)
        return chipertext

    def decrypt(self, algorithmClass, ciphertext, key, iv):
        AES_obj = AES.new(key, AES.MODE_CFB, iv)
        raw_bytes = AES_obj.decrypt(ciphertext)
        extracted_bytes = unpad(raw_bytes, AES.block_size)
        return extracted_bytes
        