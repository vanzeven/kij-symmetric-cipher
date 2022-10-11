from arc4 import ARC4


class RC4:
    def __init__(self):
        pass

    def encrypt(self, plaintext, key):
        arc4 = ARC4(bytes(key, 'utf-8'))
        cipher = arc4.encrypt(bytes(plaintext, 'utf-8'))
        return cipher

    def decrypt(self, ciphertext, key):
        arc4 = ARC4(bytes(key, 'utf-8'))
        plain = arc4.decrypt(ciphertext)
        return plain