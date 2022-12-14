import binascii
from Algorithms.DES import DES
from Algorithms.ARC4 import RC4
from Crypto.Cipher import AES
from Operations.ECBOperation import ECBOperation
from Operations.CTROperation import CTROperation
from Operations.OFBOperation import OFBOperation
from Operations.CFBOperation import CFBOperation
from Crypto.Util.Padding import pad

ciphertext = 'plaintexuntasapi'
key = 'keyaakey'

des = DES()
des.setDebug(False)

# DES Encryption
# cipherbytes = des.encrypt(bytes('plaintex', 'utf-8'), key)

# print('Cipher Bytes: ', cipherbytes)

# ECBOperation
print('ECB Operation')
ecb = ECBOperation()

print('Plain Text: ', ciphertext)

cipherbytes = ecb.encrypt(des, bytes(ciphertext, 'utf-8'), key)
print('ECB Cipher Text: ', cipherbytes)

plainbytes = ecb.decrypt(des, cipherbytes, key)
print('ECB Deciphered Text: ', plainbytes)

print()

# CTROperation
print('CTR Operation')
ctr = CTROperation()

print('Plain Text: ', ciphertext)

cipherbytes = ctr.encrypt(des, bytes(ciphertext, 'utf-8'), key, iv = 4743744)
print('CTR Cipher Text: ', cipherbytes)

plainbytes = ctr.decrypt(des, cipherbytes, key, iv = 4743744)
print('CTR Deciphered Text: ', plainbytes)

print()

# OFBOperation
ofb = OFBOperation()
key = pad(b"keykey", AES.block_size)
iv = pad(b"iviv",AES.block_size)
ciphertext = ofb.encrypt('AES', 'plaintextex', key , iv)

print('OFB Cipher Text: ', ciphertext)

# CFBOperation
cfb = CFBOperation()

# Encrypt
#key = pad(b"randomkey", AES.block_size)
#iv = pad(b"randomiv", AES.block_size)
#CFBchipertext = cfb.encrypt('AES', 'thisisplaintext', key, iv)

#print('CFB Cipher Text: ', CFBchipertext)

# RC4
RC4ciphertext = RC4().encrypt('plaintext', 'keyaakey')
print('RC4 Cipher Text: ', RC4ciphertext)
RC4plain = RC4().decrypt(RC4ciphertext, 'keyaakey')
print('RC4 Plain Text: ', RC4plain)

# Decrypt
#CFBplaintext = cfb.decrypt('AES', CFBchipertext, key, iv)
#print('CFB Plain Text: ', CFBplaintext)
