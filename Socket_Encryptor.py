from Algorithms.DES import DES
from Algorithms.RC4 import RC4

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
    # DES ECB
    return SocketEncyrptor(algorithm = DES(), operation = ECBOperation(), key = 'sapiunta', iv = None)

    # DES CTR
    # return SocketEncyrptor(algorithm = DES(), operation = CTROperation(), key = 'sapiunta', iv = 4743744)