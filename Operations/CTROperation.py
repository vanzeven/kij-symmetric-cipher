from Operations.Operation import Operation

class CTROperation(Operation):
    def __init__(self):
        pass

    def encrypt(self, algorithmClass, plaintext, key, iv):
        if len(key) != 8:
            print('Key must be 64-bit length')
            return None

        result = ''

        prime = 171923
        multiplier = 37438482
        counter = iv

        for i in range(0, len(plaintext), 8):
            counter += (iv * multiplier) % prime

            counterPlaintext = str(counter).zfill(8)

            encryptedCounter = algorithmClass.encrypt(counterPlaintext, key)

            chunk = plaintext[i:i+8]

            xoredChunk = self.xorString(chunk, encryptedCounter)

            result += xoredChunk

        return result

    def decrypt(self, algorithmClass, ciphertext, key, iv):
        pass

    def xorString(self, strA, strB):
        arrA = list(strA)
        arrB = list(strB)

        minLen = min(len(arrA), len(arrB))

        result = ''

        for i in range(minLen):
            xoredOrd = ord(arrA[i]) ^ ord(arrB[i])
            xoredChar = chr(xoredOrd)

            result += xoredChar

        return result