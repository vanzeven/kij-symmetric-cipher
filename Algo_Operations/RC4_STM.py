from arc4 import ARC4

class RC4_STM:
    def __init__(self, key, iv = None):
        self.key = key
        self.iv = None

    def encrypt(self, plaintext):
        arc4 = ARC4(self.key)
        cipher = arc4.encrypt(plaintext)
        return cipher

    def decrypt(self, ciphertext):
        arc4 = ARC4(self.key)
        plain = arc4.decrypt(ciphertext)
        return plain
        