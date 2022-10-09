from Operations.Operation import Operation
from Crypto.Cipher import AES,DES
from Crypto.Util.Padding import pad,unpad

class OFBOperation(Operation):
    def __init__(self):
        pass

    def encrypt(self, algorithmClass, plaintext, key, iv):
        data_bytes = bytes(plaintext,'utf-8')
        if (algorithmClass == 'AES'):
            padded_bytes = pad(data_bytes, AES.block_size)
            AES_obj = AES.new(key,AES.MODE_OFB,iv)
            ciphertext = AES_obj.encrypt(padded_bytes)
        else:
            padded_bytes = pad(data_bytes, DES.block_size)
            DES_obj = DES.new(key,DES.MODE_OFB,iv)
            ciphertext = DES_obj.encrypt(padded_bytes)
        return ciphertext

    def decrypt(self, algorithmClass, ciphertext, key, iv):
        AES_obj = AES.new(key,AES.MODE_OFB,iv)
        raw_bytes = AES_obj.decrypt(ciphertext)
        extracted_bytes = unpad(raw_bytes,AES.block_size)
        return extracted_bytes
