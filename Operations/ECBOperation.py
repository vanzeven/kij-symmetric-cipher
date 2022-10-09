from Operations.Operation import Operation

class ECBOperation(Operation):
    def __init__(self):
        pass

    def encrypt(self, algorithmClass, plaintext, key, iv = None):
        if len(key) != 8:
            print('Key must be 64-bit length')
            return None

        result = ''

        for i in range(0, len(plaintext), 8):
            chunk = plaintext[i:i+8]
            encryptedChunk = algorithmClass.encrypt(chunk, key)

            result += encryptedChunk

        return result

    def decrypt(self, algorithmClass, ciphertext, key, iv = None):
        pass