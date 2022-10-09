from Algorithms.DES import DES
from Crypto.Cipher import AES
from Operations.ECBOperation import ECBOperation
from Operations.OFBOperation import OFBOperation
from Crypto.Util.Padding import pad

des = DES()
des.setDebug(False)

ciphertext = des.encrypt('plaintex', 'keyaakey')

print('Cipher Text: ', ciphertext)

ecb = ECBOperation()
ciphertext = ecb.encrypt(des, 'plaintexplaintex', 'keyaakey')

print('ECB Cipher Text: ', ciphertext)

ofb = OFBOperation()
key = pad(b"keykey", AES.block_size)
iv = pad(b"iviv",AES.block_size)
ciphertext = ofb.encrypt('AES', 'plaintextex', key , iv)

print('OFB Cipher Text: ', ciphertext)