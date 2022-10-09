import binascii
from Algorithms.DES import DES
from Algorithms.RC4 import RC4
from Crypto.Cipher import AES
from Operations.ECBOperation import ECBOperation
from Operations.OFBOperation import OFBOperation
from Operations.CFBOperation import CFBOperation
from Crypto.Util.Padding import pad

des = DES()
des.setDebug(False)

# DES Encryption
ciphertext = des.encrypt('plaintex', 'keyaakey')

print('Cipher Text: ', ciphertext)

# ECBOperation
ecb = ECBOperation()
ciphertext = ecb.encrypt(des, 'plaintexplaintex', 'keyaakey')

print('ECB Cipher Text: ', ciphertext)

# OFBOperation
ofb = OFBOperation()
key = pad(b"keykey", AES.block_size)
iv = pad(b"iviv",AES.block_size)
ciphertext = ofb.encrypt('AES', 'plaintextex', key , iv)

print('OFB Cipher Text: ', ciphertext)

# CFBOperation
cfb = CFBOperation()

# Encrypt
key = pad(b"randomkey", AES.block_size)
iv = pad(b"randomiv", AES.block_size)
CFBchipertext = cfb.encrypt('AES', 'thisisplaintext', key, iv)

print('CFB Cipher Text: ', CFBchipertext)

# RC4
RC4ciphertext = RC4().encrypt('plaintex', 'keyaakey')
print('RC4 Cipher Text: ', RC4ciphertext)

# Decrypt
CFBplaintext = cfb.decrypt('AES', CFBchipertext, key, iv)
print('CFB Plain Text: ', CFBplaintext)
