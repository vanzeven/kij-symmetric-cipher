from Operations.Operation import Operation

class CTROperation(Operation):
    def __init__(self):
        pass

    def encrypt(self, algorithmClass, plaintext, key, iv):
        if len(key) != 8:
            print('Key must be 64-bit length')
            return None

        result = b''

        prime = 171923
        multiplier = 37438482
        counter = iv

        for i in range(0, len(plaintext), 8):
            counter += (iv * multiplier) % prime

            counterPlaintext = str(counter).zfill(8)
            counterPlaintext = counterPlaintext[-8:]

            encryptedCounter = algorithmClass.encrypt(bytes(counterPlaintext, 'utf-8'), key)

            chunk = plaintext[i:i+8]

            # xoredChunk = self.xorString(chunk, encryptedCounter)
            # xoredChunk = chunk ^ encryptedCounter
            xoredChunk = self.byte_xor(chunk, encryptedCounter)

            result += xoredChunk

        return result

    def decrypt(self, algorithmClass, ciphertext, key, iv):
        if len(key) != 8:
            print('Key must be 64-bit length')
            return None

        result = b''

        prime = 171923
        multiplier = 37438482
        counter = iv

        for i in range(0, len(ciphertext), 8):
            counter += (iv * multiplier) % prime

            xoredChunk = ciphertext[i:i+8]

            counterPlaintext = str(counter).zfill(8)
            counterPlaintext = counterPlaintext[-8:]

            encryptedCounter = algorithmClass.encrypt(bytes(counterPlaintext, 'utf-8'), key)

            unxoredChunk = self.byte_xor(encryptedCounter, xoredChunk)

            result += unxoredChunk

        return result

    def xorString(self, strA, strB):
        arrA = list(strA)
        arrB = list(strB)

        minLen = min(len(arrA), len(arrB))

        result = b''

        for i in range(minLen):
            xoredOrd = ord(arrA[i]) ^ ord(arrB[i])
            xoredChar = chr(xoredOrd)

            result += xoredChar

        return result

    def byte_xor(self, ba1, ba2):
        return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])