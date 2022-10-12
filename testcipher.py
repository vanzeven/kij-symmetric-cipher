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

def printCipher(algoClass):
    print('Algorithm Operation:', algoClass)

    encryptor = algoClass(key = b'sapi',iv = b'4743')
    plaintext = b'AAAAAAAAAAAAAAAA'

    ciphertext = encryptor.encrypt(plaintext)
    decryptedtext = encryptor.decrypt(ciphertext)

    print('Cipher Text: ', ciphertext)
    print('Deciphered Text: ', decryptedtext)
    print()

printCipher(AES_CBC)
printCipher(AES_CFB)
printCipher(AES_CTR)
printCipher(AES_ECB)
printCipher(AES_OFB)

printCipher(DES_CBC)
printCipher(DES_CFB)
printCipher(DES_CTR)
printCipher(DES_ECB)
printCipher(DES_OFB)

printCipher(RC4_STM)