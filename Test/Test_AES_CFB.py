import sys 
import time
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir) 
sys.path.insert(0, parentdir)

from Algo_Operations.AES_CFB import AES_CFB
# Runtime loop dan avearge per iteration
# Loop 100 kali
# plaintext size = 64 char
# key 8 byte
# IV 8 byte

ciphertext=None
total_time = 0
for i in range(10):
    start_time = time.time()
    for loop in range(1000):
        encryptor = AES_CFB(key = b'sapisapi',iv = b'47433474')
        ciphertext = encryptor.encrypt(b'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ' * 256)
        #print(encryptor.encrypt(b'aaaa'))
    interval_time = (time.time() - start_time)
    print("Waktu interval ke-%d adalah %s detik" % (i,interval_time))
    total_time += interval_time

average_time = total_time/10

print("Waktu rata-rata enkripsi adalah %s detik" % average_time ) 

plaintext=None
total_time = 0
for i in range(10):
    start_time = time.time()
    for loop in range(1000):
        encryptor = AES_CFB(key = b'sapisapi',iv = b'47433474')
        plaintext = encryptor.decrypt(ciphertext)
    interval_time = (time.time() - start_time)
    print("Waktu interval ke-%d adalah %s detik" % (i,interval_time))
    total_time += interval_time

average_time = total_time/10

print("Waktu rata-rata dekripsi adalah %s detik" % average_time )