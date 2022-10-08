from Algorithms.DES import DES
from Operations.CTROperation import CTROperation

des = DES()
ciphertext = des.encrypt('plaintext', 'key')

ctr = CTROperation()
ciphertext = ctr.encrypt(des, 'plaintext', 'key', 'iv')