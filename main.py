from Algorithms.DES import DES
from Operations.ECBOperation import ECBOperation

des = DES()
des.setDebug(False)

ciphertext = des.encrypt('plaintex', 'keyaakey')

print('Cipher Text: ', ciphertext)

ecb = ECBOperation()
ciphertext = ecb.encrypt(des, 'plaintexplaintex', 'keyaakey')

print('ECB Cipher Text: ', ciphertext)