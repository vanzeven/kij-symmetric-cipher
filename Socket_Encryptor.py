from Algo_Operations.AES_CBC import AES_CBC
from Algo_Operations.AES_CFB import AES_CFB
from Algo_Operations.AES_CTR import AES_CTR
from Algo_Operations.AES_ECB import AES_ECB
from Algo_Operations.AES_OFB import AES_OFB

from Algo_Operations.DES_CBC import DES_CBC
from Algo_Operations.DES_CFB import DES_CFB
from Algo_Operations.DES_CTR import DES_CTR
from Algo_Operations.DES_ECB import DES_ECB
from Algo_Operations.DES_OFB import DES_OFB

from Algo_Operations.RC4_STM import RC4_STM

class SocketEncyrptor:
    def __init__(self, algorithm, operation, key, iv):
        self.algorithm = algorithm
        self.operation = operation
        self.key = key
        self.iv = iv

    def encrypt(self, plainbytes):
        return self.operation.encrypt(self.algorithm, plainbytes, self.key, self.iv)

    def decrypt(self, cipherbytes):
        return self.operation.decrypt(self.algorithm, cipherbytes, self.key, self.iv)

def GetSocketEncryptor():
    encryptor = None

    # AES
    encryptor = AES_CBC(key = b'sapiunta',iv = b'sembaran')
    # encryptor = AES_CFB(key = b'sapiunta',iv = b'sembaran')
    # encryptor = AES_CTR(key = b'sapiunta',iv = b'sembaran')
    # encryptor = AES_ECB(key = b'sapiunta',iv = b'sembaran')
    # encryptor = AES_OFB(key = b'sapiunta',iv = b'sembaran')

    # DES
    # encryptor = DES_CBC(key = b'sapi',iv = b'semb')
    # encryptor = DES_CFB(key = b'sapi',iv = b'semb')
    # encryptor = DES_CTR(key = b'sapi',iv = b'semb')
    # encryptor = DES_ECB(key = b'sapi',iv = b'semb')
    # encryptor = DES_OFB(key = b'sapi',iv = b'semb')

    # RC4
    # encryptor = RC4_STM(key = b'sapi',iv = b'semb')

    return encryptor