from Algo_Operations.AES_OFB import AES_OFB
from Algorithms.DES import DES
from Algorithms.RC4 import RC4
from Algo_Operations.DES_CTR import *
from Operations.ECBOperation import ECBOperation
from Operations.CTROperation import CTROperation
from Operations.OFBOperation import OFBOperation
from Operations.CFBOperation import CFBOperation

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
    # ECB
    #return SocketEncyrptor(algorithm = AES(), operation = ECBOperation(), key = 'sapiunta', iv = None)
    #return SocketEncyrptor(algorithm = DES(), operation = ECBOperation(), key = 'sapiunta', iv = None)

    # CTR
    #return SocketEncyrptor(algorithm = AES(), operation = CTROperation(), key = 'sapiunta', iv = 4743744)
    #return SocketEncyrptor(algorithm = DES(), operation = CTROperation(), key = 'sapiunta', iv = 4743744)

    # AES
    return DES_CTR(key = b'sapiuntasapiunta',iv = b'sembaransembaran')